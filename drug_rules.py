# drug_rules.py


DRUG_RULES = {

    "Semaglutide": {
        "contraindications": [
            "mtc",
            "men2"
        ],

        "physician_review": [
            "pregnancy",
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
            "men2"
        ],

        "physician_review": [
            "pregnancy",
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
            "men2"
        ],

        "physician_review": [
            "pregnancy",
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
        "بارداری",

    "planning_pregnancy":
        "قصد بارداری",

    "mtc":
        "سابقه شخصی یا خانوادگی سرطان مدولاری تیروئید",

    "men2":
        "سابقه سندرم MEN2",

    "gastroparesis":
        "سابقه گاستروپارزی شدید",

    "pancreatitis":
        "سابقه پانکراتیت",

    "gallbladder":
        "سابقه بیماری یا سنگ کیسه صفرا",

    "other_glp1":
        "مصرف داروی GLP-1 دیگر"
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

    "gastroparesis":
        "وضعیت گاستروپارزی شدید نامشخص است",

    "pancreatitis":
        "وضعیت سابقه پانکراتیت نامشخص است",

    "gallbladder":
        "وضعیت بیماری یا سنگ کیسه صفرا نامشخص است",

    "other_glp1":
        "وضعیت مصرف داروی GLP-1 دیگر نامشخص است"
}