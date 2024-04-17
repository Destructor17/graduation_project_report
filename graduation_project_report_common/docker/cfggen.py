import json

with open("../../config.json", "r") as file:
    config = json.load(file)

with open("../../config/env.diplom.sty", "w") as file:
    # config['department']['']
    recendentMoreInfo = "\n    ".join(config["recendent"]["moreInfo"])
    file.write(
        f"""\def \envDiplomMinistr {{{config['ministry']}}}
\def \envDiplomEducation {{{config['education']}}}
\def \envDiplomUniversity {{{config['university']}}}
\def \envDiplomCathedra {{{config['cathedra']}}}

\def \envDiplomTitle {{{config['title']}}}
\def \envDiplomEnterprice {{{config['enterprise']}}}
\def \envDiplomNumber {{{config['number']}}}
\def \envDiplomVersion {{{config['version']}}}

\def \envDiplomCity {{{config['city']}}}

\def \envDiplomStudentGroupName {{{config['student']['groupName']}}}
\def \envDiplomStudentGroupNumber {{{config['student']['groupNumber']}}}
\def \envDiplomStudentCard {{{config['student']['card']}}}

\def \envDiplomStudentSurname {{{config['student']['surname']}}}
\def \envDiplomStudentInitials {{{config['student']['initials']}}}
\def \envDiplomStudentInfo{{{config['student']['info']}}}

% Руководитель
\def \envDiplomTeacherSurname {{{config['teacher']['surname']}}}
\def \envDiplomTeacherInitials {{{config['teacher']['initials']}}}
\def \envDiplomTeacherInfo{{{config['teacher']['info']}}}

% Консультант по экономическому разделу
\def \envDiplomEconomicSurname {{{config['economic']['surname']}}}
\def \envDiplomEconomicInitials {{{config['economic']['initials']}}}
\def \envDiplomEconomicInfo{{{config['economic']['info']}}}

% Консультант по ЕСПД
\def \envDiplomEspdSurname {{{config['espd']['surname']}}}
\def \envDiplomEspdInitials {{{config['espd']['initials']}}}
\def \envDiplomEspdInfo{{{config['espd']['info']}}}

% Рецензент
\def \envDiplomRecendentSurname {{{config['recendent']['surname']}}}
\def \envDiplomRecendentInitials {{{config['recendent']['initials']}}}
\def \envDiplomRecendentInfo{{{config['recendent']['info']}}}
\def \envDiplomRecendentMoreInfo{{\n    {recendentMoreInfo}\n}}

\def \envDiplomHeadCathedraSurname{{{config['department']['surname']}}}
\def \envDiplomHeadDepartmentInitials{{{config['department']['initials']}}}
\def \envDiplomHeadDepartmentInfo {{{config['department']['info']}}}

\def \envDiplomDateInput{{<<\\underline{{\hspace{{0.5cm}}}}>> \\underline{{\hspace{{2cm}}}} \ESKDtheYear~г.}}
"""
    )

with open("../../config/env.sty", "w") as file:
    # config['department']['']
    file.write(
        f"""\def \\No {{\\textnumero}}
\date {{{config["year"]}/месяц/день}}
"""
    )
