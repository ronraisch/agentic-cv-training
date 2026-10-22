# לחונך — הכנה, חניכה ובחינת חוקר

המסלול החדש הוא מפרט ולא מערכת CV מוכנה. לפני מחזור: השלם את SYSTEM_MAP ואת
readiness.csv עם קוד לימודי קיים. הרץ UI/API, train/eval/serve ו־notebook smoke ברשת
היעד. חלק את החבילות דרך Artifactory ותעד kernel/interpreter ו־CA trust מאושרים.
הסביבה הפנימית כבר מספקת את הסטאק לפי תיאור המשתמש; המטרה היא לבדוק בחירה והרשאות,
לא להקים מחדש OpenShift/Artifactory. אין להפוך הכנה חסרה לפרויקט של החניך.

## סגנון חניכה

בתשתיות מסבירים ומתקנים יחד. זמן GitLab הוא כ־45 דקות בתוך שעות שבוע 1: MR,
pipeline ו־job log. אין ניקוד על YAML, runner administration או שינון תפריטים.
במחקר החניך חייב להסביר השערה, מדידה והוכחה. סיכום אייג׳נט אינו הוכחה להבנה.
בכל סוף שבוע מקבלים דוח planned/actual; הבאפר אינו פרס לעוד ניסויים.

## מדרג שאלות

1. שבוע 1: חשב נקודה ב־zoom, הראה בקשה ושמירה. עזור בכל עניין גישה.
2. שבוע 2: מה morphology מוחק? למה תשובת segmentation מאוחרת מסוכנת?
3. שבוע 3: חשב TP/FP/FN, תן דוגמת future leakage ועקוב אחר artifact שנבחר.
4. שבוע 4: איפה מתאפס gradient? למה eval ו־inference_mode שניהם נדרשים?
5. שבוע 5: עקוב ב־BiFPN בשני הכיוונים; הוכח encode/decode; הסבר no-positive loss.
6. שבוע 6: פתח תא אקראי במחברת, תן input אחר ודרוש תחזית לפני הרצה.

## בחינת הסיום: ארבע שעות בתקציב

45 דקות: clean restart ו־run all, input חדש ו־hashes.
75 דקות: grilling שיטתי על המחברת: image decoding, dtype/range/device/shape,
resize/padding, features/BiFPN/heads בגלאי הלימודי, adapter של RF-DETR,
score/class mapping, decode/filter/NMS אם יש, inverse mapping, ריק ושגיאה,
serialization ושוויון לשירות. כל helper ניתן לפתיחה; לא בוחנים kernel internals בעל־פה.
45 דקות: תקלה חדשה כגון checkpoint שגוי, class offset או letterbox שונה. החניך נותן
השערה ו־reproducer, ומתקן ללא אייג׳נט. מסמכים ודיבאגר מותרים.
30 דקות: peer משחזר על פי הריפו בלבד; הסבר rollback ו־ADR.
45 דקות: משוב, רישום pass/blocked/remediation ומיקוד תרגול המשך.

ההסבר צריך לכלול מה השתנה ומה יפריך אותו, לא רק מה רץ. היכולת לומר "טרם בדקתי את
OpenShift-loaded artifact" נחשבת שיקול דעת; השער עצמו עדיין לא עובר עד בדיקה.
כל שלב מקבל 0–4: נעדר, דמו בלבד, happy path, edge cases, ראיה עצמאית/העברת ידע.
ממירים למשקלי CURRICULUM. כשל בהבנה קריטית או scientific leakage מחייב תיקון בלי
קשר לסך. retake ממוקד עם input חדש; אין חובה לחזור על שישה שבועות.

## מלכודות לבחירה מדורגת

שבוע 1: marker מוצג אך prompt נשמר בקואורדינטות המסך.
שבוע 2: מסכה מתמונה קודמת או preprocessing רק ב־eval.
שבוע 3: שורות tracks מאותו video בשני splits, או search שומר default estimator.
שבוע 4: שכבה ברשימה רגילה במקום ModuleList, או inference במצב train.
שבוע 5: anchor flatten order או zero-positive division.
שבוע 6: image נכון עם artifact ישן, או class-map שונה בין המחברת לשירות.
מזריקים אחד בכל פעם בענף לימודי; לא משנים מערכת מבצעית. רושמים מה הוזרק ומה הוחזר.

החזק את המקרים המוחזקים בעותק חונך. export_learner מסיר את instructor ואת Git history;
ודא שהמחברת הלימודית היא template, לא פתרון מלא. CI ירוק אינו מנגנון הסמכה.
