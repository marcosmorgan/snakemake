#######################
# Rule

# rule do_something:
#      input: "simple/data/input_1.txt"
#      output: "simple/res/output_1.txt"
#      shell: "cp {input} {output}"

#######################

# Rule all

# rule all:
#     input:
#       "simple/res/output_1.txt",
#       "simple/res/output_2.txt"
# 
# rule do_something:
#      input: "simple/data/input_{exp}.txt"
#      output: "simple/res/output_{exp}.txt"
#      shell: "cp {input} {output}"

##########################

# Expand

# rule all:
#     input:
#       expand("simple/res/output_{exp}.txt", exp=[1,2])
# 
# rule do_something:
#      input: "simple/data/input_{exp}.txt"
#      output: "simple/res/output_{exp}.txt"
#      shell: "cp {input} {output}"

##########################

# lambda wildcards

# rule all:
#     input:
#       expand("simple/res/output_{exp}.txt", exp=[1,2]),
#       "simple/res/table.txt"
# 
# rule do_something:
#      input: "simple/data/input_{exp}.txt"
#      output: "simple/res/output_{exp}.txt"
#      shell: "cp {input} {output}"
# 
# rule do_magic_lambda:
#      input:
#           lambda wildcards : ["{}/res/output_{}.txt".format(proj, res)
#                 for proj in [wildcards.project] for res in [1,2]]
#      output: "{project}/res/table.txt"
#      shell: "cat {input} > {output}"

##########################

# implicit wildcards {{}}

# rule all:
#     input:
#       expand("simple/res/output_{exp}.txt", exp=[1,2]),
#       "simple/res/table.txt"
# 
# rule do_something:
#      input: "simple/data/input_{exp}.txt"
#      output: "simple/res/output_{exp}.txt"
#      shell: "cp {input} {output}"
# 
# rule do_magic:
#      input: expand("{{project}}/res/output_{exp}.txt", exp=[1,2])
#      output: "{project}/res/table.txt"
#      shell: "cat {input} > {output}"
     
##########################

# Final

rule all:
    input:
      "simple/res/table.txt"

rule do_something:
     input: "simple/data/input_{exp}.txt"
     output: "simple/res/output_{exp}.txt"
     shell: "cp {input} {output}"

rule do_magic:
     input: expand("{{project}}/res/output_{exp}.txt", exp=[1,2])
     output: "{project}/res/table.txt"
     shell: "cat {input} > {output}"
     
##########################
