# אימות עדכון צוות פענוח — 23.10.2026

## נבדק בעדכון הנוכחי

- קישורי Markdown מקומיים בכל הריפו: תקינים.
- תקציב שבועי: 6×40=240; חלוקה 35 קריאה + 5 מדיה/טקסט + 144 מימוש + 16 חניכה + 40 באפר.
- תקציבי המשימות המפורטים מסתכמים ב־144 שעות ותואמים לחלוקה השבועית.
- תבנית notebook: JSON ו־cell IDs תקינים; נשארה תבנית לא ממומשת ולא מורצת.
- tools/export_learner.py: ניתוח syntax של Python ו־הרצה על יעד חדש מחוץ לריפו עברו.
- תוכן ההפצה נבדק בפועל: אין instructor/, MAINTAINERS.md או Git history; אין handouts
  של דרישות וידאו מאוחרות. מפת הפתרון לפוליגונים נשארת אצל החופף; בקשת החניך קצרה.
- חומר הקריאה/מפת הסשנים וקישורים בהפצת החניך קיימים. אין dangling links לחומר חופף.
- git diff --check: עבר.

הבדיקות בוצעו מקומית עם Python standard library, ללא התקנת תלויות או ניסיון לעקוף
את חסימת ההתקנה שתועדה בעבר. לא שונה קוד המחקר/runtime או lock התלויות המקורי.
לא הורצו מחדש pytest/ruff/MCP runtime; אין כאן טענת pass חדשה שלהם.

## גבולות הראיות

זה עדכון תיעוד, מטלות, handouts ותבניות. אין מערכת פענוח ממומשת, training results,
מודלים חדשים או inference שהורץ. החופף עדיין צריך לספק שלד מערכת/דאטה לפני מחזור.
אין גישה ל־GitLab, Confluence, OpenShift או Artifactory של הצוות; ה־Getting Started
הוא מדריך לאימות שם, לא connectivity test שכבר עבר. הזמנים הם אומדנים ללא pilot.

המסמך לחופף בדרייב והקישור לקורס הקודם לא אותרו/נקראו. מפת הסשנים היא מתכונת
מוצעת על סמך ההנחיות הגלויות, ואינה מוצגת כתוכן שאומת מול המסמך המקורי.
התיעוד הטכני של Hough/homography וכיול נבדק מול מקורות ראשוניים בקישורי SOURCES;
אין טענה שסקר עננים מלא או השוואת מודלי וידאו כבר נעשו — אלה משימות החניך.

## רשומות עבר — אינן בדיקות שבוצעו מחדש היום

# אימות עדכון מסלול החוקר — 22.10.2026

## נבדק בעדכון הנוכחי

- קישורי Markdown מקומיים: כל היעדים קיימים.
- סכומי שעות: כל שבוע 40; 35 קריאה + 5 מדיה/טקסט + 144 תרגול + 16 חניכה + 40 באפר = 240.
- תבנית מחברת: JSON תקין, cell IDs ייחודיים, ללא outputs או execution counts.
  זו תבנית לא ממומשת; inference ו־Restart & Run All שלה אינם נבדקים כהצלחה.
- תבנית GitLab CI: YAML parsed בהצלחה; אינה pipeline פעיל ולא הורצה ב־GitLab.
- validator של skills קיימים: עבר לשתי הדוגמאות. לא נטענה מכך הפעלה באייג׳נט פנימי.
- git diff --check: עבר.
- בדיקת learner export: מסירה של תבנית המחברת והחומרים המקומיים, ללא instructor או Git history.

## לא אומת כעת

התקנת `uv sync` לתלויות הציבוריות לא הושלמה: automatic approval review דחה אותה
בשל פנייה ל־PyPI במסגרת workflow המיועד גם לרשת סגורה. לא נעשה ניסיון לעקוף.
ניסיון CLI ללא התקנות, באמצעות ספריות runtime הקיימות, נעצר ב־ModuleNotFoundError
עבור httpx. לא הורצו מחדש pytest/ruff/MCP runtime ואין לייחס להם pass בעדכון הזה.
השינוי הנוכחי הוא תיעוד, מטלות ותבניות; קוד היישום והתלויות המקוריים לא השתנו.

אין גישה לרשת הצוות. GitLab פנימי, Artifactory, OpenShift, CA, NFS/PVC, VS Code,
Jupyter פנימי, SAM 2/RF-DETR/YOLO ו־pipeline אימון אמיתי לא נבדקו כאן.
מפת מערכת ה־CV היא מפרט לחונך עם נתיבים מוצעים, לא קוד שנמצא או מערכת שמומשה.
המשתמש מסר שהסטאק זמין ברשת; זו עובדה מדווחת, לא תוצאת בדיקת connectivity שלנו.
הזמנים וההיתכנות של הגלאי הלימודי דורשים pilot; אין אומדן מדוד ממחזור אמיתי.
קישור הקורס המקורי לא אותר; הפרקים המקומיים נכתבו ללא טענה למיפוי מאומת לקורס ההוא.

## רשומת אימות קודמת, שנשמרה מהגרסה המקורית

הטקסט להלן הוא דיווח קודם של הריפו, **לא ריצות שבוצעו מחדש בעדכון זה**.

### Previous validation record — 2026-10-22

Validated on Linux, CPython 3.12.14, NumPy 2.5.4, Pandas 3.0.6, MCP 2.3.0,
and optional Torch 2.14.1+cpu. Other supported Python/OS combinations were not run here.

- Locked core+dev+MCP installation: passed.
- Starter smoke/infrastructure suite: 5 passed.
- Reference contract suite: 10 core + 2 Torch tests passed.
- Starter advanced core contracts: 9 failures, 1 pass, as intended.
- Starter Torch contract suite: 2 failures, as intended.
- Real stdio MCP initialization, tool discovery, invocation and invalid-limit error: passed.
  The invalid-limit call deliberately produces an error log on stderr.
- Ruff static checks: passed.
- Python sdist and wheel build: passed.
- Wheel installed in a separate fresh environment outside checkout; downstream report: passed.
- CLI fixture report and deterministic 10,000-row CSV/SQLite generation: passed.
- Bad-review patch: git apply --check passed.
- Learner export strips instructor directory and Git history; removes instructor CI steps.
- Skill metadata and referenced files: checked; real learner/harness behavior not user-tested.

The core runtime is verified. Curriculum timing, learning outcomes and internal team tool onboarding
still require a first cohort/mentor pilot. This is not a completed student solution. Concurrency,
additional source integration, the MCP extension and final handover are intentionally assignments.
GitHub Actions configuration is included but has not run on GitHub before repository publication.
