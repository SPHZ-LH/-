str = input().strip()
strin = input().strip()

if strin in str:
    nowstr = str.replace(strin, "")
    print("result:", nowstr)
elif strin.lower() in str:
    nowstr = str.replace(strin.lower(), "")
    print("result:", nowstr)
elif strin.upper() in str:
    nowstr = str.replace(strin.upper(), "")
    print("result:", nowstr)
