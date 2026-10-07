DRUG_RULES = {

    "Semaglutide": {

        "contraindications": [
            "mtc",
            "men2",
            "hypersensitivity",
            "pregnancy"
        ],

        "physician_review": [
            "planning_pregnancy",
            "gastroparesis",
            "pancreatitis",
            "gallbladder",
            "other_glp1"
        ]
    },

    "Tirzepatide": {

        "contraindications": [
            "mtc",
            "men2",
            "hypersensitivity",
            "pregnancy"
        ],

        "physician_review": [
            "planning_pregnancy",
            "gastroparesis",
            "pancreatitis",
            "gallbladder",
            "other_glp1"
        ]
    },

    "Liraglutide": {

        "contraindications": [
            "mtc",
            "men2",
            "hypersensitivity",
            "pregnancy"
        ],

        "physician_review": [
            "planning_pregnancy",
            "gastroparesis",
            "pancreatitis",
            "gallbladder",
            "other_glp1"
        ]
    }
}


REASONS = {

    "pregnancy":
        "بارداری فعلی؛ مصرف دارو برای کاهش وزن نباید در بارداری ادامه یابد.",

    "planning_pregnancy":
        "قصد بارداری؛ زمان قطع دارو و برنامه‌ریزی درمان باید توسط پزشک بررسی شود.",

    "mtc":
        "سابقه شخصی یا خانوادگی سرطان مدولاری تیروئید (MTC)",

    "men2":
        "سابقه سندرم MEN2",

    "hypersensitivity":
        "سابقه حساسیت شدید به دارو یا اجزای آن",

    "gastroparesis":
        "علائم یا سابقه گاستروپارزی شدید",

    "pancreatitis":
        "سابقه پانکراتیت",

    "gallbladder":
        "سابقه بیماری یا سنگ کیسه صفرا",

    "other_glp1":
        "مصرف همزمان داروی GLP-1 یا داروی مشابه"
}


UNKNOWN_REASONS = {

    "pregnancy":
        "وضعیت بارداری نامشخص است",

    "planning_pregnancy":
        "وضعیت قصد بارداری نامشخص است",

    "mtc":
        "سابقه سرطان مدولاری تیروئید نامشخص است",

    "men2":
        "سابقه MEN2 نامشخص است",

    "hypersensitivity":
        "سابقه حساسیت شدید به دارو نامشخص است",

    "gastroparesis":
        "وضعیت علائم یا سابقه گاستروپارزی شدید نامشخص است",

    "pancreatitis":
        "وضعیت سابقه پانکراتیت نامشخص است",

    "gallbladder":
        "وضعیت بیماری یا سنگ کیسه صفرا نامشخص است",

    "other_glp1":
        "وضعیت مصرف داروی GLP-1 دیگر نامشخص است"
}