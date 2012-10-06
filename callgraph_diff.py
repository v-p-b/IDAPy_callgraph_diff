from sets import Set

# Get the segment's starting address
ea = ScreenEA()
callers = dict()
callees = dict()

# Loop through all the functions
for function_ea in Functions(SegStart(ea), SegEnd(ea)):
    f_name = GetFunctionName(function_ea)

    # Create a set with all the names of the functions calling (referring to)
    # the current one.
    callers[f_name] = Set(map(GetFunctionName, CodeRefsTo(function_ea, 0)))

    # For each of the incoming references
    for ref_ea in CodeRefsTo(function_ea, 0):
        # Get the name of the referring function
        caller_name = GetFunctionName(ref_ea)

        # Add the current function to the list of functions
        # called by the referring function
        callees[caller_name] = callees.get(caller_name, Set())
        callees[caller_name].add(f_name)

# Get the list of all functions
functions = Set(callees.keys()+callers.keys())
# For each of the functions, print the number of functions calling it and
# number of functions being called. In short, indegree and outdegree
for f in functions:
    print '%d:%s:%d' % (len(callers.get(f, [])), f, len(callees.get(f, [])))

