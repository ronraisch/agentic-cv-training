# שבוע 5 — לבנות ולהבין גלאי

חומר חובה: [פרק מקומי](../../docs/lessons/05-detector.md).

תקציב: 6 שעות קריאה, שעה מדיה/טקסט, 27 תרגול, 3 חניכה ו־3 באפר.
תרגול: 6 BiFPN/heads, 7 matching/loss/decode, 7 overfit ודיבוג, 7 מחברת וראיות.
ממשיכים את backbone והלולאה משבוע 4; לא מתחילים תשתית חדשה.

## מטלה

ממש ב־PyTorch גלאי קטן בסגנון EfficientDet, שלוש רמות ו־BiFPN בעל שני כיווני זרימה.
כתוב heads לסיווג ו־boxes, anchors/assignment, loss, encode/decode ו־postprocess.
מותר operations בסיסיות וספריית backbone; אסור להגיש wrapper ל־detector מוכן כמימוש.
Compound scaling וכל הגדלים של EfficientDet הם רשות מחוץ לתקציב הבסיסי.

בדוק כל רכיב בנפרד: shapes גם בגדלים אי־זוגיים, weights נרשמים ונשמרים, gradients,
anchor order, encode/decode inverse, zero positives, no GT ו־NMS. הראה overfit על
דאטה זעיר לפני ניסוי held-out מוגבל. שמור טווח התוצאות והגבלות ההכללה.

## מחברת והגנה ראשונה

העתק את `templates/notebooks/operational-inference.ipynb` לנתיב המחברת שבמיפוי הפנימי.
השלם על הגלאי שכתבת: טעינה, preprocess, feature maps, BiFPN, heads, decode, overlay.
שמור raw outputs והסבר כל shape וטרנספורמציה. Restart & Run All ללא state קודם.
החונך יפתח גם פונקציות מיובאות וישאל על שורה אקראית ומקרה empty/odd-size.

## קבלה

artifact/reload מוכחים; בדיקת מסלול יחיד מול batch; מחברת ניתנת להרצה, ADR להבדלים
מהמאמר ו־run log. אין דרישת COCO performance או טענה שזה EfficientDet מלא.

## דרך העבודה בכל שלב

קרא את הפרק המקומי והקוד שהחונך מיפה. לפני אייג׳נט: כתוב תחזית, חוזה ומבחן מפריך.
עבוד עם האייג׳נט על שינוי תחום; בדוק diff, הרץ והסבר בעצמך. שמור MR, ADR כשנדרש,
יומן ניסוי ו־`templates/claim-evidence.md`. מצב mock/מקומי/פנימי מסומן בכל ראיה.
טענה שלא נבדקה נשארת "טרם אומת". לא מציגים תרגיל סינתטי כעבודה היסטורית של הצוות.
