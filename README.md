# חפיפת חוקר — Research Engineering with AI

**שישה שבועות, ריפו אחד, פיתוח עם אייג׳נט והוכחות להבנה.**

[מתחילים כאן](docs/START_HERE.md) · [תוכנית שש־שבועית ותקציב שעות](docs/CURRICULUM.md)
· [Getting Started ברשת הסגורה](docs/GETTING_STARTED_INTERNAL.md)
· [פרקי לימוד מקומיים](docs/lessons/README.md) · [מפת המערכת](docs/SYSTEM_MAP.md)

| שבוע | תוצר עיקרי |
|---|---|
| 1 | סביבה עובדת, GitLab בסיסי ושינוי קטן בתיוג |
| 2 | תיוג בנקודה דרך שירות ושינוי preprocessing קלאסי |
| 3 | evaluation ו־XGBoost לסיווג tracks של YOLO |
| 4 | אימון ודיבוג PyTorch עם הוכחת gradients ו־save/reload |
| 5 | גלאי לימודי בסגנון EfficientDet עם BiFPN ומחברת ראשונה |
| 6 | החלפת YOLO11 ב־RF-DETR, מחברת inference מבצעי והגנה לעומק |

240 שעות: 35 קריאה/ניתוח קוד, 5 וידאו או חלופת טקסט, 144 תרגול ותיעוד, 16 חניכה
ובחינה ו־40 התארגנות/רשת/תקלות. הזמנים אומדנים; אין קורס מלא נוסף מחוץ לתקציב.

התוכן מתוחזק בחוץ ב־GitHub ומיועד גם ל־GitLab פנימי ללא אינטרנט. Python מנוהל ב־uv;
בפנים משתמשים ב־Artifactory ובסטאק הקיים של הצוות: VS Code, Jupyter, Docker ו־OpenShift.
Getting Started מלמד מה להריץ, מה לצפות לראות ואיך לטפל בכשל יחד עם החונך.
GitLab CI/CD מקבל היכרות קצרה בלבד: MR, pipeline ו־job log.

## מה כבר קיים ומה דורש הכנת חונך

קיים קוד ResearchLab סינתטי: retrieval/embedding, NumPy/Pandas/SQLite/HTTP, Torch בסיסי,
MCP ו־skills. הוא מכיל פגמים מכוונים. מעבדות הפיתוח המקוריות נשמרו ומשולבות בתוכנית.
מערכת ה־CV (תיוג, YOLO, tracks, train/eval/serve) היא **מפרט למערכת חפיפה**, לא מימוש
שכבר נבדק כאן. החונך מספק שלד עובד או ממפה מערכת צוות באותו ריפו לפני המחזור.
[רשימת הכנה ומגבלות](docs/SYSTEM_MAP.md) · [סטטוס אימות](docs/VALIDATION.md).

```bash
uv sync --extra dev --extra mcp --locked
uv run researchlab
uv run pytest
uv run python tools/check_mcp.py
```

הפקודות מתייחסות למסלול הסינתטי הקיים ול־lock החיצוני. בתוך הרשת עובדים לפי מדריך
הסביבה הפנימי. החבילות למערכת ה־CV אינן מותקנות על ידי הפקודה הזו.

[מלכודות](docs/PITFALLS.md) · [עבודה עם אייג׳נט](docs/AGENT_WORK.md)
· [מקורות רשות](docs/SOURCES.md) · [מדריך חונך](instructor/RESEARCH_GUIDE.md)
· [תבנית מחברת](templates/notebooks/operational-inference.ipynb)

הגרסה הקודמת נשמרת בענפים `v1.0.0` ו־`archive/v1-development-only`.
קוד וטקסט מקוריים: MIT. אין העתקת קורסים או טענה לתמיכה מטעם מוסדות המקור.
