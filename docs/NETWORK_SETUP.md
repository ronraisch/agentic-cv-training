# הכנת הרשת והמשאבים — לחיבור מודרך

לפי תיאור המשתמש הסטאק זמין בפנים: VS Code, Jupyter, Docker, OpenShift, GitLab,
Artifactory, Confluence וחבילות המחקר. לא בונים מחדש את התשתיות.
החניך עובד לפי GETTING_STARTED_INTERNAL; החופף ממלא readiness.csv ומפת סביבה פנימית.
לכל חסימה: בעלים, תאריך בקשה, בדיקה הבאה וחלופה. אין כתובות/סודות פנים בעותק הציבורי.

| משאב | סימן הצלחה |
|---|---|
| GitLab | clone ו־commit צפוי; MR ו־job log |
| VS Code | סביבת uv נכונה ו־breakpoint שנעצר |
| Python/uv דרך Artifactory | lock פנימי, imports וריצה ללא download ציבורי |
| Jupyter | kernel נכון ו־Restart & Run All |
| Confluence | דף צוות נפתח ואפשר למצוא את המידע ובעליו |
| Docker/registry | image פנימי רץ עם output/digest ידועים |
| OpenShift | workload לימודי Ready ובקשת route עם fixture נכון |
| NFS/PVC | נתון נשמר ונקרא לאחר restart בסביבת הלימוד |
| דאטה ומשקלים | manifests והגרסאות הזמינות ל־LPR, tracklets, scoring ו־video encoder |
| כלי אייג׳נט | skills/MCP נבחרים נטענים בפועל עם trace חיובי וכשל מבוקר |

ב־Python משתמשים ב־uv בלבד. החופף מכין lock/index/CA פנימיים לפני המחזור; lock ציבורי
יכול לכלול כתובות artifacts ציבוריות. --offline הוא בדיקת cache ולא תחליף לחיבור
ל־Artifactory פנימי. wheel למערכת אחרת או תלות עקיפה חסרה נבדקים בלי לשנות גרסה בשקט.
ה־lock הקיים בריפו הוא של ResearchLab, לא סביבת פענוח מלאה.

חבילת העברה רק לפריט חסר כוללת שם, גרסה/commit, hash, platform, dependencies,
model/config/caches, fixtures ורישוי נדרש. אין הורדות runtime. יש דוגמת no-network
smoke פנימית שהחופף מאמת, ואין צורך שהחניך יכין registry או ירכיב תשתית.

40 שעות באפר מחולקות 18/8/4/4/3/3 לפי השבוע. תקלות תשתית לומדים עם החופף.
מימוש, דיבוג וניסויים רגילים כלולים בזמן התרגול. אם אין גישה לשירות פנימי, לא מסמנים
פריסה כ־PASS בזכות container מקומי, ומציינים מה עדיין חסום.
