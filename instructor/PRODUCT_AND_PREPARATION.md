# מפת הכנה פנימית — לא למסירה מראש לחניך

כל הנתיבים כאן מוצעים, לא מימוש שקיים בריפו. החופף ממפה לפני המחזור לקוד עובד.

| אזור | נתיב מוצע | דרישת הכנה / קבלה |
|---|---|---|
| אתר תיוג | apps/labeling | rectangle עובד, zoom/pan ושמירת נתונים ישנים |
| API/data | services/labeling, data/annotations | schema אמיתי, גרסאות, fixture ישן/חדש ו־migration test מוחזק |
| צרכן אימון | training/crops, training/dataset | loader/export שמחובר לנתונים; החלטת crop אינה מוכתבת לחניך מראש |
| LPR | src/lpr, services/lpr | detector/recognizer קפואים, baseline ותמונות מגוונות |
| חיבור תמונות | src/imagery | שני pairs עם overlap ועוד no-overlap/parallax |
| tracklets | src/motion | timestamps, labels, camera info ו־group IDs |
| ניקוד | src/rescoring | frozen detections, GT ו־GSD/angle conventions |
| עננים | research/clouds | מקורות/דאטה זמינים לבדיקה; אין דרישה למודל מוכן |
| וידאו | src/video, services/video | clips, embedding weights, model factory וחוזה שירות בסיסי |
| פריסה | deploy | image פנימי, namespace לימודי, route ו־storage |

בחומר החניך משאירים מפת שירותים נייטרלית, לא checklist שמגלה את מטלת הפוליגונים.
לתיעוד חופף משתמשים ב־RESEARCH_GUIDE; למסירה לפי סדר משתמשים ב־releases/.
