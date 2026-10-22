# שבוע 4 — אימון ודיבוג PyTorch

חומר חובה: [פרק מקומי](../../docs/lessons/04-torch.md).

תקציב: 8 שעות קריאה, שעה מדיה/טקסט, 24 תרגול, 3 חניכה ו־4 באפר.

## מטלה

בנה dataset/dataloader, backbone קטן ולולאת אימון PyTorch. התחל classification קטן
על אותו דאטה/fixture כדי לא לערבב בעיית אופטימיזציה עם matching של detector.
זה בסיס שישמש בשבוע 5, לא פרויקט צד נפרד או עוד מודל שיש לכוון ימים.

הצג shapes/dtypes/devices, בדוק parameter update ו־gradient flow, overfit ל־2–8 תמונות,
שמור וטען ל־instance חדש. הכן את שלוש רמות התכונות שיצטרכו להתחבר ל־BiFPN.
אינך נדרש לשחזר EfficientNet מאפס; מותר backbone לימודי קטן ומתועד.

אתר ותקן שלוש תקלות שהחונך בוחר: module לא רשום, gradient accumulation, dtype/device,
train בזמן inference, reshape שגוי או checkpoint אחר. תעד minimal reproducer ותוצאה
מפריכה; אין תגמול על זמן מבוזבז בלוגים.

## קבלה והסבר

קוד נפרד למחקר חוזר, config ו־run manifest; גרפי loss ו־gradient norm;
שוויון save/reload בטולרנס; בדיקת eval/inference ומקרה empty.
ללא אייג׳נט עקוב אחרי batch עד optimizer ותקן תקלה חדשה קטנה. הסבר למה loss יורד
אינו הוכחה להכללה, ואילו בדיקות יתבצעו לפני הגדלת האימון.

## דרך העבודה בכל שלב

קרא את הפרק המקומי והקוד שהחונך מיפה. לפני אייג׳נט: כתוב תחזית, חוזה ומבחן מפריך.
עבוד עם האייג׳נט על שינוי תחום; בדוק diff, הרץ והסבר בעצמך. שמור MR, ADR כשנדרש,
יומן ניסוי ו־`templates/claim-evidence.md`. מצב mock/מקומי/פנימי מסומן בכל ראיה.
טענה שלא נבדקה נשארת "טרם אומת". לא מציגים תרגיל סינתטי כעבודה היסטורית של הצוות.
