# מלכודות כלליות בחפיפת מחקר

זו רשימת ידע רוחבית, לא הוראות פתרון לבקשות הפרודקט. לכל כשל בחר input מפריך
וראיה. החופף עשוי לשאול על כשל גם אם לא נדרש במימוש הספציפי שלך.

| מלכודת | מה עלול להיראות תקין | מה לבדוק |
|---|---|---|
| תיעוד ישן | סיפור ארכיטקטורה משכנע | caller/config נוכחיים ומסלול שרץ |
| agent API מומצא | wrapper שנראה מקצועי | גרסה מותקנת ו־smoke אמיתי |
| test שמשכפל מימוש | suite ירוק | oracle עצמאי ו־counterexample |
| exception נבלע | פלט ריק סביר | הבדל בין error, unknown ו־negative |
| RGB/BGR, range/dtype | תמונה נראית דומה | values ידועים בכל גבול |
| Hough על פרטי פנים | קווים חזקים | האם הם הגבולות הנכונים וקיימת גאומטריה יציבה |
| homography לא מתאימה | seam נחמד | נקודות בקרה, parallax ו־no-overlap |
| רק דוגמאות שהצליחו | שיפור LPR גדול | denominator מלא כולל failed rectification/fallback |
| video/scene leakage | מדדים גבוהים | group-disjointness וקטעים/tiles חופפים |
| future feature | tracklet קל לסיווג | מידע זמין ברגע החלטה בלבד |
| sensor shortcut | metadata משפר | slices, ablations וסנסור/גיחה שלא נראו |
| מידות/angle לא מוגדרים | כלל פיזיקלי משכנע | GSD, units, projection, partial object וכיוון angle |
| score מוצג כהסתברות | PR השתפר | objective של דירוג מול בדיקת calibration |
| search שמר default | tuning מוצלח | estimator נבחר→artifact→מודל שנטען |
| head מול encoder חדש | checkpoint נטען | versions, feature schema ו־cache key |
| train בזמן inference | תוצאות לא יציבות | eval וגם no-grad/inference scope |
| gradient לא מגיע | loss זז | norm ו־parameter delta לרכיב הרצוי |
| רק pixel IoU לעננים | segmentation טובה | חיסכון נטו ופגיעה באובייקטים עקב gating |
| ענן נחשב אפס אובייקטים | תשובה חלקה לצרכן | לא נצפה מול אין זיהויים |
| sampling מעלים אירוע | פריימים ברורים | סדר/זמן ו־event eval |
| labels חסרים הם negatives | training פשוט | annotation mask ו־unknown policy |
| VLM עונה בביטחון | מלל תקין | truth, parsing, unsupported question ו־versioning |
| cache/hidden state | notebook עובד | clean restart ו־input חדש |
| green CI בלבד | תחושת סיום | אילו commands רצו, skipped ומה לא נבדק |
| mutable image tag | deployment חדש לכאורה | digest ו־loaded artifact בפועל |
| filesystem של pod | שמירה מקומית הצליחה | storage ו־קריאה לאחר restart בסביבת לימוד |

תקלות תשתית לומדים במודרך. תקלות שמשנות מסקנת מחקר מחייבות הבנה, reproducer וראיה.
אין חובה שמודל חדש ינצח; חובה לדעת מה הראיות מאפשרות להסיק ומה הן עדיין לא מוכיחות.
