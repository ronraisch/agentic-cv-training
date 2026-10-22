# 5 — גלאי לימודי בסגנון EfficientDet

EfficientDet משלב backbone, BiFPN לאיחוד תכונות במספר scales, ו־heads לקטגוריות
ולתיבות. כאן מממשים גרסה קטנה ב־PyTorch. זו מטלת בנייה, לא טענה שאין מימושי EfficientDet
מוכנים בעולם; האיסור על ספריית detector מוכנה הוא בחירה פדגוגית.

## backbone וריבוי רמות

backbone קטן מפיק C3/C4/C5 ברזולוציות שונות. לדוגמה תמונת 256×256 יכולה להפיק
32×32, 16×16, 8×8 עם strides של 8,16,32. מפרידים stride מרוחב הערוצים: לפני fusion
ממפים ערוצים לרוחב משותף באמצעות projection. אובייקט קטן עשוי להיעלם ברמה גסה;
upsampling של feature map אינו מחזיר מידע שלא נצפה. מודדים slices של גדלים ולא
מציגים multi-scale כפתרון קסם לאובייקטים תת־פיקסליים.

## BiFPN

עושים מעבר top-down שמביא הקשר מרמה גסה לרמה עדינה, ואחריו bottom-up שמחזיר מידע
עדין לרמות גסות. בכל node מיישרים resolution וערוצים לפני איחוד. אפשר להשתמש
במשקלים נלמדים לא שליליים: output = sum(relu(w_i)*x_i)/(epsilon+sum(relu(w_i))).
כאן epsilon מונע חלוקה באפס; normalization מונע הגדלת הסקאלה רק בגלל מספר קלטים.
אחרי fusion יש convolution; בגרסה הלימודית מתעדים אם היא separable או רגילה.
כל מסלול חייב להופיע ב־forward וב־graph, ולא רק בתרשים README.

בדיקות מבודדות: input קבוע בעל ערך שונה לכל רמה כדי לזהות מקור; shapes במספר גדלים
כולל מימד אי־זוגי; gradients דרך שני הכיוונים; weights רשומים ונשמרים. ב־nearest/bilinear
upsampling משתמשים ב־target size מפורש כדי למנוע הבדל של פיקסל בחיבור.
שלוש רמות והיקף קטן הם adaptation מתועד, לא שחזור מלא של טבלאות המאמר.

## heads, anchors ו־matching

בכל מיקום מנבאים A anchors: class logits [B,A*K,H,W] ו־box deltas [B,A*4,H,W].
לאחר flatten כל חיזוי חייב להתאים לאותו anchor באותו סדר. החלפת סדר reshape בלבד
יכולה לתת boxes שגויות בלי exception. מתחילים ביחס aspect וסקאלה מוגבלים ומתועדים.

anchor מקבל positive/negative/ignore לפי IoU וכלל assignment מוגדר. צריך כלל גם
לתמונה בלי GT וגם ל־GT שלא קיבל anchor חיובי. אין להכריח את כל anchors להיות negative
כשיש בעיית mapping. box encoding, לדוגמה deltas של center ו־log width/height, חייב
להיות הופכי ל־decode. בדקו encode→decode על תיבות ידועות לפני אימון.

loss סיווג יכול להיות focal loss שמפחית משקל easy negatives; regression מחושב על
positives בלבד עם normalization מתועד. כשאין positives מחזירים loss regression
תקין שמאפשר backward ומונעים division by zero. IoU loss או smooth-L1 הן בחירות שיש
לנמק ולשמור עקביות עם הייצוג. loss יורד לא פוטר מבדיקה ויזואלית.

## inference

לפי הסדר: image→resize/pad/normalize→backbone→BiFPN→heads→decode→score filtering
→class-aware NMS אם הוגדר לגלאי→inverse transform→clip→schema. מסבירים כל shape,
threshold והנחה. NMS suppresses overlapping predictions, אך אינו מתקין label mapping.
לא מפעילים אוטומטית אותו NMS על RF-DETR רק מפני של־YOLO היה אחד.

מחברת צריכה להראות intermediate tensors, output table, overlays, תמונה ריקה,
שחזור טעינה ו־batch/single parity. כותבים את החישוב המשותף במודולים שהשירות משתמש בהם,
ומציגים במחברת את הפירוט הנחוץ להבנה; אין לשכפל preprocess מתחרה בתוך המחברת.
החונך רשאי לפתוח כל פונקציה שיובאה ולשאול כיצד היא פועלת.
