# שבוע 3 — מדדים ו־XGBoost למסלולים

חומר חובה: [פרק מקומי](../../docs/lessons/03-metrics-ml.md).

תקציב: 6 שעות קריאה, שעה מדיה/טקסט, 27 תרגול, 2 חניכה ו־4 באפר.
תרגול: 8 שעות evaluator, 13 features/ML, ו־6 reproducibility ותיקונים.

## evaluation לפני tuning

ממש או תקן את שכבת evaluation סביב המימוש שהוכן: בדיקות ידניות ל־TP/FP/FN,
כפילות, תמונה ריקה, class mapping ו־IoU. הפק PR, AP לפי פרוטוקול מפורש ו־slices.
אפשר להשתמש בספריית evaluator מוכנה; צריך להבין ולבדוק את semantics שלה.

## מסווג tracks

קבל tracks מ־YOLO ותיוגים נפרדים. הגדר target, רגע החלטה ותכונות זמינות באותו רגע.
פצל לפי video/scene/session, לא פריימים או track IDs בלבד אם tracks מאותו וידאו מתואמים.
התחל baseline threshold/majority ומודל פשוט; אמן XGBoost בתקציב קטן של ניסויים שהוגדר
מראש. בחר hyperparameters/threshold על validation בלבד; הקפא לפני test.

שמור feature schema, class map, splits ו־artifact. טען instance חדש והרץ דרך ה־API
המיועד, על אותן features בדיוק. צור בכוונה mismatch של column order/פרמטר שמירה
והראה שבדיקה עצמאית מזהה אותו. אם מזריקים דוגמת SVM C, עקוב מ־search עד loaded model.

## קבלה והסבר

טבלת השוואה ל־baseline, confusion matrix, דוגמאות טעויות, טענות מסומנות ו־hashes.
בדיקה ששתי קבוצות הפיצול זרות והיעדר future features; הוכחת loaded artifact.
ללא אייג׳נט חשב matching קטן והסבר למה מודל יכול "להצליח" כשיש leakage.
זו מטלת דוגמה רלוונטית; לא נטען שזו בדיוק משימה היסטורית בצוות בלי ראיה.

## דרך העבודה בכל שלב

קרא את הפרק המקומי והקוד שהחונך מיפה. לפני אייג׳נט: כתוב תחזית, חוזה ומבחן מפריך.
עבוד עם האייג׳נט על שינוי תחום; בדוק diff, הרץ והסבר בעצמך. שמור MR, ADR כשנדרש,
יומן ניסוי ו־`templates/claim-evidence.md`. מצב mock/מקומי/פנימי מסומן בכל ראיה.
טענה שלא נבדקה נשארת "טרם אומת". לא מציגים תרגיל סינתטי כעבודה היסטורית של הצוות.
