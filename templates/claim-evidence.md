# טענה וראיה

- טענה:
- סטטוס: נצפה / מוסק / טרם אומת / חסום
- היקף: קוד / ריצה מקומית / container / שירות פנימי
- קובץ ו־commit, פקודה, input ID ופלט:
- מה הראיה אינה מוכיחה:
- בדיקה שעשויה להפריך את הטענה:
- owner ופעולה הבאה:

## שרשרת artifact

data/split hash → training config בפועל → run ID → בחירת checkpoint/estimator
→ saved hash → image digest → loaded hash/config בשירות → request ID → prediction.
כל חוליה לא נבדקת מסומנת בנפרד; אין לשדרג את כל השרשרת ל"נצפה".
