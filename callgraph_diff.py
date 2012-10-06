from sets import Set

def GetRefToSet(to_func,s=Set()):
    s.add(GetFunctionName(to_func))
    for r in CodeRefsTo(to_func,1):
        if GetFunctionName(r) not in s:
            #print("%s @ %x" % (GetFunctionName(r),LocByName(GetFunctionName(r))))
            GetRefToSet(LocByName(GetFunctionName(r)),s)
    return s

# Get the segment's starting address
ea = ScreenEA()
funcA=ChooseFunction("Please select function A").startEA
funcB=ChooseFunction("Please select function B").startEA

callersA=Set()
callersB=Set()


print "Caller list of function A:"
GetRefToSet(funcA,callersA)
print callersA
print "Caller list of function B:"
GetRefToSet(funcB,callersB)
print callersB

print "Common callers:"
print callersA & callersB

print "A-B:"
print callersA - callersB
print "B-A:"
print callersB - callersA


