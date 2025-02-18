import subprocess

base = r"""\documentclass[convert]{standalone}
\begin{document}    
\begin{tabular}{cc}
\multicolumn{2}{c}{xyz_NAME_zyx} \\
cups    & grams \\
\hline
1 & xyz_1CUP_zyx \\
3/4 & xyz_34CUP_zyx \\
2/3 & xyz_23CUP_zyx \\
1/2 & xyz_12CUP_zyx \\
1/3 & xyz_13CUP_zyx\\
1/4 & xyz_14CUP_zyx\\
tbs    & grams \\
4 & xyz_4TBS_zyx \\
3 & xyz_3TBS_zyx \\
2 & xyz_2TBS_zyx \\
1 & xyz_1TBS_zyx \\
\end{tabular}
\end{document}
"""

print(base)

substances = {
    "water": 237,
    "flour": 150,
    "sugar": 200,
    "milk": 245,
    "cocoa": 84,
    "powdered sugar": 112,
    "butter": 227,
    "vegetable oil": 220,
    "baking soda": 255,
    "honey": 3 * 113,
    "ketchup": 4 / 3 * 198,
    "mayo": 4 * 54,
    "coconut oil": 2 * 113,
    "peanut butter": 2 * 129,
    "brown sugar": 2 * 106,
    "corn syrup": 4 * 85,
    "blue corn flour": 128,
    "apple sauce": 265,
    "chocolate chips": 183,
    "yogurt": 244,
    "cottage cheese": 2 / 3 * 395,
}

for key, cup_grams in substances.items():
    print(key)
    tex = base
    tex = tex.replace("xyz_NAME_zyx", key)
    tex = tex.replace("xyz_1CUP_zyx", str(round(cup_grams)))
    tex = tex.replace("xyz_34CUP_zyx", str(round(3/4*cup_grams)))
    tex = tex.replace("xyz_23CUP_zyx", str(round(2/3*cup_grams)))
    tex = tex.replace("xyz_12CUP_zyx", str(round(1/2*cup_grams)))
    tex = tex.replace("xyz_13CUP_zyx", str(round(1/3*cup_grams)))
    tex = tex.replace("xyz_14CUP_zyx", str(round(1/4*cup_grams)))
    tex = tex.replace("xyz_4TBS_zyx", str(round(4/16*cup_grams)))
    tex = tex.replace("xyz_3TBS_zyx", str(round(3/16*cup_grams)))
    tex = tex.replace("xyz_2TBS_zyx", str(round(2/16*cup_grams)))
    tex = tex.replace("xyz_1TBS_zyx", str(round(1/16*cup_grams)))

    tex_name = f"{key}.tex"
    with open(tex_name, "w") as stream:
        stream.write(tex)
    subprocess.run(["pdflatex", "--shell-escape", tex_name])
    print("  Done!")
