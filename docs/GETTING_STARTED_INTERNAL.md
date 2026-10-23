# Getting Started מודרך — רשת סגורה, GitLab והסטאק הפנימי

**מטרה:** בסוף התהליך אתה עובד ב־VS Code וב־Jupyter עם אותה סביבת Python,
מריץ fixture, שומר תוצאה, ויודע איפה לראות אם ההרצה והפריסה הצליחו.
החונך מלווה את הבדיקות. זה שיעור בתשתיות העבודה, לא מבחן DevOps.
לפי תיאור הצוות הסטאק והחבילות קיימים ברשת: לא מתקינים מחדש את התשתיות.
בודקים שאתה מחובר למשאבים הנכונים ושיש לך הרשאות.

הזמן כלול בשבוע 1 ובבאפר של שישה שבועות. העבודה המדויקת בשירות CV מחייבת שלד
שהחונך מספק; בינתיים אפשר להוכיח את סביבת Python עם ResearchLab הקיים.

## לפני שמתחילים — החונך ממלא פעם אחת

ב־`templates/internal-environment.example.md` מלא את הכתובות הפנימיות, project/namespace,
image ו־artifact לימודיים, path של NFS/PVC, branch, health path ופקודת הפעלת UI/API.
החזק עותק מלא בריפו GitLab הפנימי בלבד. בחוץ שומרים דוגמאות ריקות בלי כתובות/פרטי צוות.
אין להשתמש בכתובת ציבורית כחלופה אוטומטית. סרטון חייב להיות זמין ברשת הפנימית או
להתחלף בפרק הטקסט המקומי; הקישורים ב־SOURCES הם רשות בלבד.

לכל שלב רשום: מה עשית, מה ציפית, מה ראית, מצב PASS/BLOCKED, ואם חסום — למי פנית.
אל תשמור tokens, קובצי kubeconfig או לוגים עם סודות. החונך מספק את פרטי ההתחברות בדרך
המקובלת אצלכם. פקודות shell להלן הן דוגמאות Linux/Bash; החונך מתאים לתחנת העבודה.

## 1. לפתוח את הפרויקט ב־GitLab וב־VS Code

**בצע:** פתח את הכתובת הפנימית שהחונך נתן. בדף הפרויקט בחר Code/Clone והעתק את
כתובת SSH או HTTPS המאושרת. בתיקיית העבודה הרץ `git clone` עם הכתובת הזו, ואז פתח
את התיקייה ב־VS Code (File → Open Folder). אין צורך לשכפל מ־GitHub מתוך הרשת.

```bash
git status
git remote -v
git log -1 --oneline
```

**צפוי:** branch ידוע, working tree clean, remote פנימי ו־commit שהחונך סימן.
**הצלחה:** קובץ README המקומי זהה לגרסה שנבחרה ב־GitLab וניתן לפתוח Terminal באותה תיקייה.
**אם נכשל:** "not a git repository" — אתה בתיקייה הלא נכונה; שם מארח לא נפתר — בדוק
רשת/DNS פנימיים; certificate — בקש CA ארגוני מאושר; permission denied — בדוק identity
והרשאת פרויקט עם החונך. אין צורך להבין GitLab CI/CD כדי להתקדם.

## 2. Python ו־uv מהמשאבים הפנימיים

```bash
python --version
uv --version
```

**צפוי:** Python 3.11 ומעלה עבור ResearchLab וגרסת uv שהחונך אישר.
החונך נותן configuration ל־Artifactory/index הפנימי, CA ו־lock המתאים לרשת.
ה־`uv.lock` הציבורי עשוי להכיל כתובות artifacts ציבוריות; הוספת index לפקודה בלבד
אינה הוכחה שה־lock לא ינסה להשתמש בהן. החונך מכין branch/config/lock פנימי תואם,
שומר את ה־lock החיצוני בגרסתו, ומאמת סביבה חדשה בלי אינטרנט.
לא מבצעים re-lock אקראי אצל כל חניך ולא מורידים installer מהאינטרנט.

אחרי שהחונך אישר שה־lock וה־index הפנימיים מוגדרים:

```bash
uv sync --extra dev --extra mcp --locked
uv run --no-sync python -c 'import sys, numpy, pandas; print(sys.executable); print(numpy.__version__, pandas.__version__)'
```

**צפוי:** sync מסתיים ללא שגיאה; executable מתוך סביבת הפרויקט; גרסאות לפי lock.
**הצלחה:** import עובד מתוך סביבת הפרויקט בלי תלות ב־Python מערכת אחר.
**אם נכשל:** 401/403 — authentication/authorization ל־repository; TLS — CA trust;
חבילה לא נמצאת — בדוק שם/גרסה/index ומערכת הפעלה עם החונך. לא לעקוף TLS.
אם מופיע ניסיון לגשת ל־pypi.org או host ציבורי, עוצרים ומתקנים את הגדרת התלות עם החונך.

רשת סגורה עם Artifactory **אינה מחייבת** `--offline`: הדגל מונע גם גישה למשאבים
פנימיים שעוד לא נמצאים ב־cache. משתמשים בו רק לבדיקת cache מוכן. החניך לומד את
ההבחנה הזו, לא נדרש להכין בעצמו wheelhouse או תשתית registry.

## 3. לבחור interpreter ב־VS Code

**בצע:** Command Palette → Python: Select Interpreter → סביבת הפרויקט `.venv`.
פתח קובץ Python, שים breakpoint ב־pipeline והריץ את פקודת הדיבוג שהחונך מספק.

**צפוי:** אותו `sys.executable` כמו בשלב 2; debugger עוצר ב־breakpoint ומראה shape.
**הצלחה:** import עובד גם מתוך editor/debugger, לא רק ב־Terminal.
**אם נכשל:** הרחבת Python חסרה — התקן מהמקור הפנימי עם החונך; interpreter אחר — בחר
מחדש; Remote/SSH — פתח את התיקייה וההרחבה בצד הנכון. אין מתקינים הרחבה ציבורית כשאין גישה.

## 4. Jupyter — לבדוק kernel ולא רק שהדף נפתח

פתח Jupyter או notebook ב־VS Code בהתאם להנחיית הצוות. בחר kernel של סביבת הפרויקט;
אם חסרה הרשמה החונך משתמש ב־ipykernel הזמין פנימית. Jupyter/ipykernel אינם כרגע
extras של ResearchLab; משתמשים בסביבת notebook שהחונך הכין, לא מניחים ש־uv sync התקין אותם.

הרץ בתא חדש:

```python
import sys
import numpy as np
print(sys.executable)
x = np.array([[3.0, 4.0]])
print(x.shape, np.linalg.norm(x, axis=1).tolist())
```

**צפוי:** interpreter תואם; הפלט `(1, 2)` ו־`[5.0]`.
שמור את המחברת, בצע Restart Kernel ואז Run All.
**הצלחה:** הפלט זהה אחרי restart, ואין צורך בתאים ישנים שלא נשמרו.
**אם נכשל:** kernel שגוי — בחר סביבת פרויקט; import חסר — בדוק executable לפני התקנה;
שמירה נכשלת — בדוק path והרשאות, לא שומרים רק בטאב פתוח. כתובת Jupyter עם token אינה נכנסת ל־MR.

## 5. Smoke של קוד מוכר

```bash
uv run --no-sync researchlab
uv run --no-sync pytest
uv run --no-sync python tools/check_mcp.py
```

**צפוי לפי הגרסה הבסיסית:** CLI מחזיר JSON של fixture; suite בסיסי: 5 passed;
בדיקת MCP מאשרת initialization/discovery/tool call וגם דחיית limit לא חוקי.
הודעת שגיאה עבור limit לא חוקי היא חלק מהבדיקה, לא קריסה בלתי צפויה.
**הצלחה:** פקודות מסתיימות בקוד יציאה 0; שמור output ו־commit. אלו smoke tests בלבד:
הקוד מכיל פגמים לימודיים ו־5 passed אינו אישור שכל המערכת נכונה.
**אם נכשל:** ודא cwd ו־interpreter, lock וגרסת MCP. השווה עם החונך ל־fixture הצפוי.
אין לפתוח את פתרונות instructor כחלק מהאבחון העצמי.

במערכת ה־CV המוכנה חזור על פקודת fixture שהחונך מילא: צפוי מספר תמונות ופלט מוכר,
לא רק exit code מוצלח. בדוק UI→API→שמירה→טעינה. בלי שלד מוכן השער הזה BLOCKED.

## 6. Docker ו־Artifactory — תרגיל עם image לימודי מאושר

```bash
docker version
```

**צפוי:** גם Client וגם Server זמינים; אם משתמשים במנגנון אחר בצוות החונך נותן פקודה
מקבילה. Client בלבד ושגיאת daemon אינה הצלחה. החונך מספק image פנימי קטן ופקודת run
שמוציאה `ONBOARDING_OK` ומסתיימת ללא שינוי שירותי אמת.

**בצע עם החונך:** pull ל־image פנימי ידוע, run לפי המתכון, ואם הרשאה רלוונטית — build/tag/push
לתיקיית לימוד ייעודית ו־pull בחזרה. אין להשתמש ב־`hello-world` ציבורי או base image ציבורי.
**צפוי:** הפלט המדויק מהמתכון, exit code 0, ו־digest שמתאים ל־image שנבחר.
**הצלחה:** image באמת רץ; "pull complete" בלבד לא מוכיח runtime תקין.
**אם נכשל:** daemon/socket — בדוק זמינות והרשאה עם החונך; unauthorized — בדוק registry
והרשאה; manifest unknown — tag/path; timeout — host/DNS/route; TLS — trust store מאושר.
לא נותנים הרשאות מערכת גורפות כפתרון אוטומטי.

## 7. OpenShift — להכיר deployment עובד בעזרת החונך

CLI או web console, לפי המקובל בצוות. אם CLI זמין:

```bash
oc whoami
oc project
oc get pods
oc get svc
oc get routes
```

**צפוי:** זהות שלך, namespace לימודי שהוקצה, workload לימודי שמגיע ל־Ready,
service ו־route ידועים. לא צריך לפרוס cluster או לכתוב מניפסטים מאפס.
**בצע:** פתח workload, בדוק image digest ו־logs, פתח את route ו־health path שהחונך
סיפק. הרץ בקשת fixture שמציגה model/artifact ID ופלט צפוי.
**הצלחה:** בקשה מחוץ ל־pod מגיעה לשירות ומחזירה את fixture וה־artifact הנכונים.
Running בלבד או health 200 אינם מוכיחים את החישוב הזה.
**אם נכשל:** ImagePullBackOff — image/path/pull permission; CrashLoopBackOff — פתח logs;
service ללא endpoints — selector/Ready; route לא עונה — host/TLS/target port; 403 — הרשאה.
החונך מסביר ועוזר. אין חובה לזכור שמות מצבים לבחינה.

## 8. שמירה וקריאה מחדש ב־NFS/PVC

**בצע:** שמור annotation או קובץ probe בנתיב הלימודי שהחונך נתן. סגור ופתח מחדש את
האפליקציה וקרא אותו. בהנחיית החונך בלבד, אתחל workload לימודי ובדוק שהנתון נשאר.
אין לבצע restart למערכת מבצעית כחלק מהתרגיל.
**צפוי:** אותה רשומה/אותו checksum לאחר restart, בנתיב ה־PVC ולא בתיקייה זמנית של container.
**הצלחה:** persistence הודגם. זה אינו מבחן גיבוי או התאוששות מכל כשל.
**אם נכשל:** ודא mount/path, UID והרשאות, PVC bound ומנגנון הכתיבה; פנה לחונך.

## 9. Confluence — להגיע לידע של הצוות

**בצע עם החופף:** פתח את הכתובת הפנימית שסופקה, התחבר בדרך המאושרת וחפש את דף
הכניסה לצוות/נהלי העבודה שנבחר. פתח דף נוסף דרך קישור פנימי וחזור לעמוד הכניסה.
החופף מסביר איפה מוצאים owners, מידע על שירותים וקישור לריפו.

**צפוי:** שם הדף ותוכנו תואמים למה שהחופף הראה; אינך רואה רק דף login או Access denied.
**הצלחה:** תוכל לפתוח ולמצוא שוב את דף הידע לאחר סגירת הטאב. רשום title/קישור
בעותק הפנימי. אין צורך לייצא תוכן פנימי אל GitHub; חומר חובה לימודי נשמר בריפו המקומי.
**אם נכשל:** DNS/timeout — בדוק רשת פנימית; לולאת login — SSO/session עם החופף;
403 או דף חסר — בדוק הרשאת Space/Page וקישור מעודכן. צפייה מספיקה אלא אם החופף
הגדיר גם עריכה כדרישת תפקיד; אל תבקש הרשאות ניהול כדי לפתוח מסמך.

## 10. GitLab בקטנה — כ־45 דקות, בתוך שעות החניכה/תרגול של שבוע 1

1. צור branch לימודי, בצע commit קטן ו־push ל־remote הפנימי.
2. פתח Merge requests → New merge request, בחר source/target ותן הסבר קצר וראיות.
3. בלשונית Changes קרא את השינוי; בדוק שאין generated files או סודות.
4. פתח את קישור ה־pipeline ב־MR או Build/CI/CD → Pipelines (השם משתנה בין גרסאות).
   בחר pipeline לאותו commit, ואז job כדי לראות log. החונך מדגים שורת command ותוצאתה.
5. מצא status, השגיאה הראשונה ו־artifacts אם קיימים. Retry רק ל־job בטוח שהחונך בחר;
   אין ללחוץ deploy/manual על סביבה מבצעית כחלק מההיכרות.

**צפוי:** MR מציג branch/commit נכון, ויש תוצאה מוסברת של job: passed/failed/skipped/blocked.
**הצלחה:** אתה יודע למצוא review ולוג ולהביא לחונך שגיאה רלוונטית. failed עשוי להיות
כשל אמיתי; pending/stuck יכול להיות תור/runner חסר; skipped אינו passed.
אם בפרויקט אין pipeline, החונך מראה pipeline לימודי מוכן; לא מטילים על החניך לבנות CI.
אין דרישה ללמוד runners, YAML או CI/CD architecture. הגדרת GitLab נמצאת ב־templates
לחונך, וה־GitHub Actions החיצוני אינו הוכחה שה־GitLab הפנימי הוגדר.

## דף הצלחה מסכם

- [ ] GitLab פנימי ו־clone בגרסה ידועה.
- [ ] uv/import מתוך index ו־lock פנימיים מאושרים.
- [ ] VS Code debugger ו־Jupyter משתמשים בסביבה הנכונה; מחברת שורדת restart.
- [ ] fixture/tests/MCP רצים עם פלט צפוי והיקף ידוע.
- [ ] image פנימי רץ; digest ו־פלט המתכון תואמים.
- [ ] workload לימודי Ready, ובקשת route מבצעת חישוב צפוי.
- [ ] שמירה וקריאה לאחר restart על storage המתאים.
- [ ] Confluence: דף כניסה ודף עבודה נפתחו, וניתן למצוא אותם שוב.
- [ ] MR, pipeline ו־job log נמצאו והוסברו.

החונך משלים איתך כל סעיף. חסימה מתועדת אינה כישלון בהבנת מחקר; היא גם אינה PASS.
אין מהירות־הקלדה או ציוני תשתית. המטרה להתחיל לעבוד בביטחון ולזהות למי לפנות.
