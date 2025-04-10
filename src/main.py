import subprocess
import sys

def execute_cmd_str_direct(name):
    """convert to list"""
    subprocess.run(f"echo 'Hello, {name}!'", shell=True)

def execute_cmd_str_var(name):
    """convert var to list"""
    the_cmd = f"echo 'Hello, {name}!'"
    subprocess.run(the_cmd, shell=True)

def execute_cmd_str_var_multi_line(name):
    """convert var to list"""
    the_cmd = f"echo 'Hello, {name}!' " \
                "a very long command" \
                "with multiple lines" \
                "finish with" + name
    subprocess.run(the_cmd, shell=True)

def execute_cmd_str_var_concat(name):
    """convert var to list"""
    base_command = "echo"
    the_cmd = base_command + f"'Hello, {name}!'"
    subprocess.run(the_cmd, shell=True)

def execute_cmd_str_var_with_other_usages(name):
    """cannot change the type of the_cmd, so no fix"""
    the_cmd = f"echo 'Hello, {name}!'"
    subprocess.run(the_cmd, shell=True)
    return the_cmd

def execute_cmd_list_direct(name):
    """already a safe list, fp"""
    subprocess.run(["echo", f"Hello, {name}!"], shell=True)

def execute_cmd_list_var(name):
    """already a safe list, fp"""
    the_cmd = ["echo", f"Hello, {name}!"]
    subprocess.run(the_cmd, shell=True)

def execute_cmd_list_var_concat(name):
    """already a safe list, fp"""
    the_cmd = ["echo", f"Hello, {name}!"] + ["a", "b"]
    subprocess.run(the_cmd, shell=True)

def execute_cmd_list_var_first_element_is_vuln(name):
    """no fix since the first element is vuln"""
    the_cmd = [f"{name}", f"Hello, {name}!"]
    subprocess.run(the_cmd, shell=True)

def execute_cmd_unknown_var(the_cmd):
    """no fix since the_cmd is unknown"""
    subprocess.run(the_cmd, shell=True)

def execute_cmd_unknown_var2(name):
    """no fix since the_cmd is unknown"""
    the_cmd = _get_cmd(name)
    subprocess.run(the_cmd, shell=True)

def _get_cmd(name):
    return f"echo 'Hello, {name}!'"


def execute_cmd_str_var_with_several_assignments(name):
    """cannot change the type of the_cmd, to avoid breaking other usages"""
    the_cmd = f"echo 'Hello, {name}!'"
    the_cmd = f"echo 'Welcome, {name}!'"
    subprocess.run(the_cmd, shell=True)

some_global_cmd = "cmd"
subprocess.run(some_global_cmd, shell=True)

def execute_cmd_global_var():
    """no fix since some_global_cmd is unknown"""
    subprocess.run(some_global_cmd, shell=True)

def execute_cmd_global_var2(name):
    """no fix since some_global_cmd is unknown"""
    subprocess.run(some_global_cmd, shell=True)
    some_global_cmd = f"echo 'Hello, {name}!'"  # must not fix this string

if __name__ == "__main__":
    execute_cmd_str_direct(sys.argv[1])
    execute_cmd_str_var(sys.argv[1])
    execute_cmd_str_var_multi_line(sys.argv[1])
    execute_cmd_str_var_concat(sys.argv[1])
    execute_cmd_str_var_with_other_usages(sys.argv[1])
    execute_cmd_list_direct(sys.argv[1])
    execute_cmd_list_var(sys.argv[1])
    execute_cmd_list_var_concat(sys.argv[1])
    execute_cmd_list_var_first_element_is_vuln(sys.argv[1])
    execute_cmd_unknown_var(sys.argv[1])
    execute_cmd_unknown_var2(sys.argv[1])
    execute_cmd_str_var_with_several_assignments(sys.argv[1])
    execute_cmd_global_var()
    execute_cmd_global_var2(sys.argv[1])
