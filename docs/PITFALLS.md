# מלכודות חובה — מכל שלב עד פרויקט הסיום

בכל MR מציינים אילו שורות רלוונטיות, איך בדקו, ומה נשאר לא מאומת.

| מלכודת | תוצאה מטעה | בדיקה מפריכה / ראיה |
|---|---|---|
| README או ADR ישן | "ככה זה עובד" בלי שהמסלול מחובר | trace בקוד ב־commit הנוכחי ובקשה אמיתית |
| tuning נשמר למודל אחר | search הצליח, production נשאר default | selected estimator→saved hash→loaded parameters→request |
| שינוי class-map | מדד מתקבל על classes אחרים | roundtrip IDs ו־overlay עם שמות ידועים |
| resize/pad/inverse שונים | boxes נראות סבירות ומוסטות | מלבן ידוע על גדלים שונים כולל padding |
| RGB/BGR/range/dtype | שינוי שקט ב־features | פיקסלי צבע ידועים ו־min/max בכל גבול |
| mask interpolation | נוצרות תוויות לא חוקיות | assert על set IDs ו־overlay על מקור |
| preprocessing רק במחברת | train/serve שונים | אותה פונקציה/גרסה והשוואת fixture בשלושת המסלולים |
| split לפי rows/frames | leakage ו־metric מנופח | group-disjointness לפי video/scene/session |
| track feature מהעתיד | הצלחה offline בלתי ניתנת להפעלה | חתוך מסלול ברגע החלטה והשווה features |
| many-to-many join או סדר עמודות | אובדן זהות/תיוג | uniqueness/cardinality ו־shuffle של rows/columns |
| שימוש ב־test לבחירת פרמטר | test הפך validation | פרוטוקול הקפאה, tuning log ו־test חד־פעמי |
| כפילות סביב GT | recall/TP מנופחים | חיזוי כפול עם התאמה חד־חד־ערכית |
| AP שונה בין ספריות | השוואה בלתי תקפה | אותו evaluator, thresholds, ignored policy ו־class map |
| רק accuracy | מיעוט נעלם | confusion/PR ו־slice עם המכנה |
| exception הופך לפלט ריק | outage נראה "אין אובייקטים" | outage fixture עם סטטוס שגיאה נפרד |
| פלט ישן בבקשת תיוג | מסכה שייכת לתמונה אחרת | החלפת תמונה בזמן request ומעקב IDs |
| model.train בזמן serving | dropout/BN משנים תוצאות | eval+inference, repeatability ובדיקה לפני/אחרי |
| loss בלי gradients לחלק מהגלאי | loss יורד אך BiFPN קפוא | norms ו־parameter delta בכל רכיב |
| anchor flatten/encode order | boxes שגויות ללא exception | oracle ידני ו־encode/decode inverse |
| zero GT/positives | NaN או model collapse | batch ריק עם backward finite |
| strict=False מסתיר head חסר | checkpoint "נטען" עם head אקראי | missing/unexpected keys והוכחת config |
| NMS מועתק אוטומטית | RF-DETR מקבל עיבוד לא מתאים | בדיקת backend contract והשפעת postprocess בנפרד |
| cache מגרסה ישנה | תוצאה נראית מהירה ונכונה | image/model/preprocess hashes ב־key ובדיקת invalidation |
| job/pipeline ירוק בלבד | בדיקה לא רצה או לא בנתיב הנכון | job command, output, skipped checks ו־commit SHA |
| image tag mutable | pod טוען משהו אחר | image digest ו־artifact hash מתוך השירות |
| filesystem של pod | annotations נעלמים ב־restart | persistence דרך PVC ובדיקה לאחר restart |
| mock מושלם | חוזה copied עם אותה טעות | דוגמה ידנית ומסלול אמיתי נפרד |
| notebook עם hidden state | עובד רק אצל הכותב | Restart & Run All בסביבה נקייה |
| זמן GPU בלי sync/warm-up | latency לא מייצג | protocol זהה וחלוקה model/I/O/end-to-end |
| agent המציא API | wrapper נראה תקין אך לא רץ | installed version/signature ו־smoke אמיתי |
| skill נמצא אך לא נטען | מניחים guardrails לא פעילים | trace חיובי וגם negative trigger |

החונך בוחר 3–4 תקלות מדורגות לאורך המסלול, ועוד תקלה חדשה בסוף; לא מכניסים את כל
הטבלה כמלכודות סודיות ביום הראשון. טעות תשתית נלמדת במודרך; טעות שמשנה מסקנת מחקר
דורשת מהחניך לזהות ולהוכיח את התיקון. אין תגמול על ניחוש בטוח או על ציון benchmark לבדו.
