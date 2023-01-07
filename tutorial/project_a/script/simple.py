rule all:
    input:
          expand("project_a/res/output_{exp}.txt", exp=[1,2,3]),
          "project_a/res/final_table.csv"

rule do_something:
     input: "{project}/data/input_{exp}.txt"
     output: "{project}/res/output_{exp}.txt"
     shell: "cp {input} {output}"
     
rule do_magic:
     input: 
          expand("{{project}}/res/output_{exp}.txt", exp=[1,2,3])
     output: "{project}/res/final_table.csv"
     shell: "cat {input} > {output}" 
