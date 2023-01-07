rule all:
    input:
          expand("simple/res/output_{exp}.txt", exp=[1,2]),
          "simple/res/final_table.csv"

rule do_something:
     input: "{project}/data/input_{exp}.txt"
     output: "{project}/res/output_{exp}.txt"
     shell: "cp {input} {output}"
     
rule do_magic:
     input: 
          lambda wildcards : ["{}/res/output_{}.txt".format(proj, res) 
                for proj in [wildcards.project] for res in [1,2]]
     output: "{project}/res/final_table.csv"
     shell: "cat {input} > {output}" 

# rule do_simple_magic:
#      input: 
#           expand("{{project}}/res/output_{exp}.txt", exp=[1,2])
#      output: "{project}/res/final_table.csv"
#      shell: "cat {input} > {output}"
