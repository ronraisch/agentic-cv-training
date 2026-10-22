# 6 — החלפת backend והוכחת inference מבצעי

החלפת YOLO11 ב־RF-DETR היא קודם כול שינוי בגבול מודל. מזהים מי קורא predict, איזה
schema נצרך, איך class IDs נבנים, מה נשמר ומה ה־evaluator מקבל. implementation plan
צריך להפנות לנתיבי הקוד שנבדקו בפועל. adapter אינו מקום להסתיר תוצאות חריגות.
אין הבטחה שההחלפה פשוטה עד שבודקים dependencies, משקלים, גודל קלט, latency ויצוא.

משאירים בחירה מפורשת ב־config בין backends. כל אחד משתמש ב־preprocess וב־decode
שלו ומחזיר boxes במקור ו־class map מוסכם. runtime API נקבע לפי הגרסה הפנימית המותקנת;
דוגמה באינטרנט מגרסה אחרת אינה spec. loss/assignment של RF-DETR אינם בהכרח כמו
הגלאי anchor-based שכתבנו. אין להעתיק optimizer, NMS ו־threshold באופן עיוור.

## השוואה שניתן לפרש

מקפיאים test split ומדדי הצלחה לפני בדיקה. מספקים baseline YOLO11 שמור, fine-tune
קצר ל־RF-DETR או checkpoint שאושר למשימה, training smoke וטעינה חוזרת. אם אימון
איכות מלא חורג מהזמן, מציינים שההשוואה מוגבלת ושאין מסקנת עליונות.
מודד עצמאי עם אותו split מפיק PR/AP, slices (אובייקטים קטנים, negatives, דחיסות),
ומספר תמונות/GT. latency נמדד באותה חומרה, batch, precision, warm-up ומדיניות I/O;
מפרידים זמן network/preprocess/model/postprocess. ב־GPU מסנכרנים את המדידה לפי הצורך.
משקלים טובים יותר עם evaluator אחר אינם ראיה לשיפור במערכת הזו.

## chain מהמחברת לשירות

config→model factory→checkpoint hash→preprocess revision→prediction→postprocess→API
response. מחברת שעושה inference על checkpoint אחר אינה תיאור המסלול המבצעי.
מריצים אותו fixture במחברת, בפונקציית השירות וב־endpoint ומבצעים התאמה בטולרנס
מוצהר; מקבלים גם artifact ID מהשירות. containers מזוהים לפי digest, לא רק tag mutable.
בדיקת NFS/PVC בוחנת restart והרשאות; annotations אינם נשמרים רק ב־filesystem של pod.

תוצאת פרויקט יכולה להיות "ה־adapter נכון אבל איננו ממליצים להחליף בגלל recall/latency".
זו מסקנת מחקר תקינה. נדרשת אפשרות rollback ל־YOLO11 ובדיקה שהוא עדיין עובד.
שירות פנימי שלא נבדק נשאר חסום גם אם local container והמחברת עברו.

## המחברת אינה צילום מסך

Restart & Run All בסביבה נקייה, path/config מפורשים, no hidden state, ללא download
runtime. מציגים input, artifact, tensor shapes/ranges/devices, intermediate stages,
raw/filtered outputs, overlay ומקרה שגיאה. מוסיפים הסבר קצר לפני כל block ולינק למימוש.
החניך יודע למה כל שורה נחוצה ומה יישבר אם ישנה אותה. אין חובה לכתוב מחדש ספריות,
אבל "ה־package עושה את זה" אינו מספיק כששואלים על transform או סף קריטי.
