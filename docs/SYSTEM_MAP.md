# מערכת החפיפה: עובדות, תכנון ונקודות כניסה

## סטטוס שנבדק ב־22.10.2026

ב־main בנקודת ההתחלה `060ca34` קיימים CLI, pipeline אחזור/embedding סינתטי,
NumPy/Pandas/SQLite/HTTP, דוגמת Torch ושרת MCP. **אין** שם עדיין אפליקציית תיוג,
אימון YOLO11, tracks, evaluator לגלאים או שירות inference פרוס. המשימות החדשות הן מפרט
לחפיפה על מערכת כזו; אין להסיק מהמפרט שהמערכת כבר מומשה או נבדקה ברשת הצוות.

## הכנה שחייבת להסתיים לפני תחילת המחזור

החונך מספק באותו ריפו עותק לימודי עובד או קישור פנימי ממופה לקוד הצוות: UI בתיוג,
API, דוגמת תיוג ושמירה, baseline YOLO11, פלטי tracks, נתוני split, evaluator,
אימון וטעינת artifact, Dockerfile ומניפסטים פנימיים. כל נתיב בטבלה בהמשך מסומן
PROPOSED עד שמחליפים אותו בנתיב אמיתי וב־commit שנבדק.
לא מצפים מהחניך לבנות את כל השלד תוך כדי תרגיל של 14 שעות.
יש להריץ preflight ולספק דגימת קלט/פלט; בלי זה השבוע הראשון חסום. בסיס המחקר הקיים
יכול לשמש לאבחון Python בזמן ההמתנה, אך אינו שקול לאינטגרציית תיוג/גלאי.

| אזור | נקודת כניסה מוצעת, לא קוד קיים | מי משתמש בו | ראיית חיבור נדרשת |
|---|---|---|---|
| Labeling UI | `apps/labeling/` React + TypeScript | מתייג | קליק בדפדפן, request ID ושמירה/טעינה |
| Labeling API | `services/labeling/` Python | UI | schema, segmentation provider, מזהה תמונה |
| Preprocessing | `src/vision/preprocess.py` | train/eval/serve | אותה גרסה והגדרות בשלושת המסלולים |
| Dataset/splits | `datasets/manifests/` | train/eval | checksum, group IDs, class map |
| Train | `training/` | חוקר | config בפועל, checkpoint נבחר והסיבה לבחירה |
| Models | `src/vision/models/` | train ו־predict | YOLO/RF-DETR/adaptor לגלאי הלימודי |
| Evaluation | `evaluation/` | חוקר ו־CI | matching, PR, slices ו־latency protocol |
| Serving | `services/inference/` | צרכן downstream | artifact hash ונתיב request אמיתי |
| Deploy | `deploy/` | Docker→Artifactory→OpenShift | digest→pod→service→route, PVC/NFS |
| ידע מחקרי | `research/adr/`, `research/logs/` | החוקר הבא | החלטה, חלופה, ראיה, תנאי לבחינה מחדש |
| מחברת | `notebooks/operational-inference.ipynb` | חוקר וחונך | Restart & Run All ופריטי evidence |

## חוזה גלאי משותף

קלט ציבורי: image_id, תמונת RGB H×W×3 uint8 בגודל המקורי, batch מוגבל ו־model ID.
כל backend מבצע בתוכו את ה־resize/normalization הנדרשים לו, ומחזיר לחוזה אחיד:
boxes float32 [N,4] ב־xyxy בפיקסלים של המקור; scores [N] בטווח [0,1]; class_ids [N]
לפי class map ממוספר ומתועד. פלט ריק הוא [0,4] ו־[0], לא None ולא שגיאת שירות מוסתרת.
לכל תשובה מצרפים model/artifact/preprocessing/class-map revisions וסטטוס.
אפשר לעדכן חוזה אם לקוד האמיתי יש ממשק אחר; מתעדים זאת לפני מימוש adapter.
אין לכפות normalization אחד על כל גלאי; השוואה הוגנת שומרת על משמעות התמונה והפלט,
ומאפשרת לכל backend את העיבוד הדרוש לו.

## טענות ומידת ודאות

כל טענה משמעותית מסומנת: **נצפה** (קובץ+commit או ריצה ופלט), **מוסק** (הנחות),
**טרם אומת** (הבדיקה החסרה), או **חסום** (בעלים ופעולת שחרור).
קריאת קוד מוכיחה מה כתוב, לא שזה המסלול שרץ. בדיקה מקומית אינה פריסה.
דוגמה: "נצפה: search בחן C; טרם אומת: האם best_estimator הוא ה־artifact שנטען בשירות".
הוכחה מלאה דורשת search results→בחירה→שמירה→hash→container→loaded model→בקשה
ואותה הגדרה גם בתשובה המבצעית. בטוחים בכוח הראיות, לא לפי אחוז שהאייג׳נט המציא.
