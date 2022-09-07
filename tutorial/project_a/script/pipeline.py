rule all:
    input:
          expand("project_a/res/output_{exp}.txt", exp=[1,2,3]),
          "project_a/res/final_table.csv"

rule do_more:
     input: "{project}/inter/view_{exp}.txt"
     output: "{project}/res/output_{exp}.txt"
     shell: "run new_command {input} {output}"

rule do_something:
     input: "{project}/data/input_{exp}.txt"
     output: "{project}/inter/view_{exp}.txt"
     params: 10
     shell: "your_command -p {params} {input} {output}"

def magic(wildcards):
  return expand("{proj}/inter/view_{exp}.txt", 
               proj = wildcards.project, 
               exp=[1,2,3])

rule do_magic:
     input: magic
     output: "{project}/res/final_table.csv"
     shell: "command {input} {output}"    

