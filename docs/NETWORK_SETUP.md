# Getting Started ברשת והעברות — 40 שעות באפר לכל המסלול

## יום ראשון: בודקים גישה לתלויות הקיימות

הסטאק זמין ברשת לפי תיאור הצוות; בודקים קישור והרשאה, ומעבירים רק פריט חסר.
המדריך לחניך הוא GETTING_STARTED_INTERNAL.md; רשימה זו מיועדת בעיקר להכנת החונך.

החונך והחניך ממלאים `templates/readiness.csv`. לכל חסימה: בעלים, תאריך בקשה,
מה חסר, חלופה מקומית ומועד בדיקה הבא. אין לכתוב כתובות פנימיות או סודות בגרסה ציבורית.
החונך מחזיק רשימת מיפוי פנימית באותו עותק ריפו שבו עובדים בתוך הרשת.

| מה להכין | איך מוכיחים זמינות | חלופה בזמן עיכוב |
|---|---|---|
| Git, סביבת Python ו־uv | clone פנימי ו־uv sync עם lock מקומי | סביבת ההוראה הקיימת |
| wheelhouse/index פנימי וכל תלות עקיפה | התקנה בסביבה נקייה ללא אינטרנט | תרגילי NumPy וניתוח קוד |
| React/TS, Node וחבילות frontend | lockfile ו־build מתוך registry/cache פנימי | בדיקת API וחוזי קואורדינטות |
| Torch וחבילת accelerator תואמת | import, device, forward/backward זעיר | CPU על fixture קטן |
| OpenCV, XGBoost, evaluator, notebook | import ופקודת smoke לפי lock מאושר | חישובים קטנים וכתיבת oracle |
| YOLO11/RF-DETR/SAM 2 אם נבחר | קוד, config, משקלים וכל cache תלוי זמינים בלי download | ספק סגמנטציה קלאסי; RF-DETR נשאר חסום אם חסר |
| fixtures ונתונים | manifest, hashes, annotations, splits ונתוני tracks | synthetic מתאים עם תיוג ברור |
| אייג׳נט, skills ו־MCPs | session trace שמראה טעינה וקריאת כלי אמיתית | תיעוד ו־MCP המקומי; שער פנימי עדיין חסום |
| Artifactory ו־OpenShift | push/pull של image ו־pod ברשת היעד | container מקומי; לא נחשב פריסה פנימית |
| service/route ו־PVC/NFS | request מבחוץ וקריאה לאחר restart | בדיקה מקומית; מחיקת pod אינה בדיקת גיבוי |

## נוהל חבילת העברה

מכינים manifest: שם, גרסה/commit, פלטפורמה, מטרה, hash, תלות, בעלים וסטטוס.
כוללים גם transitive dependencies, משקלים, configs, tokenizers/backbones אם צריך,
נתוני smoke, מדריכים מקומיים ורישוי נדרש להעברה. הורדות runtime אסורות כמנגנון תלות:
מריצים smoke ברשת מבודדת ומחפשים ניסיון חיבור. אין לשנות version כדי "שיעבור" בלי
לשמור מה השתנה; wheel למערכת/ארכיטקטורה אחרת אינו תחליף תקין.

`uv sync --extra dev --extra mcp --locked` הוא למסלול הקיים. אין כרגע lock מלא
ל־UI/SAM 2/XGBoost/גלאים: החונך מכין ומאמת אותו לפני המחזור. אין לטעון שהפקודה
מתקינה את רכיבי המערכת המוצעים. uv הוא מנהל Python היחיד; frontend משתמש ב־lock
של כלי ה־Node שנבחר. `--offline` דורש cache מוכן מראש ואינו יוצר אותו.

## פענוח תקלת פריסה

בודקים לפי הסדר: image digest נכון; image pull; startup logs; config בפועל;
service selector ופורט; route ו־health; artifact path/hash; UID והרשאות PVC;
כתיבה/קריאה מחדש לאחר restart. לא מתקנים 403 או mount failure באמצעות fallback
לקובץ זמני שמאבד תיוגים. API חי אינו ראיה שהמשקלים הנכונים נטענו.

הבאפר הוא 18/8/4/4/3/3 שעות לפי השבוע. פתיחת בקשה והמשך לימוד יכולים להתקיים
במקביל בזמן קלנדרי, אבל אין לזקוף את אותו זמן לשתי קטגוריות. עיכוב שמעבר לתקציב
נחשף בדוח השבועי; אין להבטיח סיום ברשת בלי גישה אליה.
