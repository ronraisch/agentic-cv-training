# 4 — PyTorch שצריך להבין בידיים

טנזור הוא נתונים עם shape, dtype, device ולעיתים graph לחישוב נגזרות.
NCHW אינו NHWC: תמונת [H,W,3] צריכה permute מתועד ואז batch, לא reshape שמערבב
פיקסלים. Conv2d מחבר ערוצים ומחליק kernel במרחב; stride משנה רזולוציה. כתבו shapes
לכל שכבה לפני הרצה. batch size אינו מספר classes ו־numel אינו גודל הזיכרון בבתים.

## לולאת אימון

לכל batch: קלט ו־targets על אותו device; איפוס gradients לפי מדיניות accumulation;
forward; loss; backward; optimizer.step. gradients מצטברים כברירת מחדל. אם שוכחים
zero_grad מתקבל אלגוריתם אחר. detach או מעבר ל־NumPy באמצע loss יכול לנתק gradient.
loss שנראה סביר אינו מוכיח שכל head לומד: בדקו gradient norms ופרמטר שהשתנה.
בחירת loss צריכה להתאים ל־logits/targets: sigmoid נוסף לפני loss שמצפה logits משנה
את הבעיה. קובעים reduction כדי לא להפוך מספר anchors למשקל משתנה בין batches.

`train()` ו־`eval()` שולטים בהתנהגות כגון dropout ו־BatchNorm; הם אינם כיבוי autograd.
`no_grad`/`inference_mode` מונעים בניית graph אך אינם מחליפים eval. בפונקציה שמבטיחה
לא לשנות מצב למשתמש, משחזרים אותו גם ב־exception. metric על outputs שמוחזקים ב־GPU
עלול לשמור graph/זיכרון בין batches. לצבירת דוח מעבירים תוצרים נחוצים ומנותקים ל־CPU.

## סדר דיבוג

1. בדקו batch ו־overlay של GT לפני מודל. הוסיפו דוגמת empty ו־nonfinite.
2. ריצה forward אחת עם shapes ו־range. ודאו loss finite, matching ותוויות.
3. backward אחד: gradient מגיע לרכיבים הרצויים ו־step משנה פרמטר.
4. overfit על 2–8 תמונות קבועות בלי augmentation. יעד מפורש: ירידה ב־loss ושיפור
   boxes/סיווג על אותן תמונות; אינו הוכחת הכללה. אי־הצלחה מחזירה ל־data/loss/assignment.
5. save, טעינה ל־instance חדש, eval ותחזיות תואמות בטולרנס שנקבע.
6. רק אז batch גדול, augmentation או GPU. seed אינו מבטיח שוויון בין כל פלטפורמות.

## שגיאות שצריך להרגיש

מזריקים באופן מבוקר: target float במקום class index כש־loss דורש integer; שכבה שלא
נרשמה כ־ModuleList ולכן לא מופיעה ב־parameters; device mismatch; train בזמן inference;
resize של תמונה בלי boxes; שימור outputs עם gradients. לכל אחת רושמים סימפטום,
הנחה שנשברה, reproducer קטן וראיה לתיקון. לא מסתפקים ב־try/except שמעלים אותה.

checkpoint הוא החלטה מחקרית: שומרים architecture/config, class map, preprocess,
state_dict, data/split provenance, epoch וקריטריון בחירה. optimizer state נחוץ להמשך
אימון אמיתי; inference אינו צריך אותו. טעינת משקל חלקית עם strict=False יכולה להסתיר
head אקראי: מדווחים missing/unexpected keys ולא מגדירים זאת "נטען בהצלחה".

תרגיל הסבר: עקבו מתא בתמונה אל activation, loss, gradient ופרמטר. לאחר restart
הסבירו איך נבנה model זהה ואיזה קובץ מחייב את זה. הסבירו איך אותו עיקרון חל על head מעל embedding ועל מודל segmentation.
