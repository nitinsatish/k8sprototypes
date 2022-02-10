# calgary
tkg3 = ["1.18.0", "1.19.0", "1.20.0"]
tkg3_tkr = {
             "1.18.0":[ "ant", "cal", "fl" ],
             "1.19.0":[ "ant 1.0 2.0 3.", "cal 1.0", "fl" ],
             "1.20.0":[ "ant 1.0 2.0 3.0", "cal", "fl" ]
}

# dakar
tkg4 = ["1.19.0", "1.20.0", "1.21.0"]
tkg4_tkr = {
             "1.19.0":[ "ant ( 1.0, 1.1 ) ", "cal ( 1.0, 1.1 )", "fl"], # pinnipied, ako both bump minors
             "1.20.0":[ "ant ( 2.0 2.1) ", "cal", "fl" ]
             "1.21.0":[ "ant", "cal", "fl", "d" ]
}




tkg5 = ["1.20.0", "1.21.0", "1.22.0"]

############################################

# Week 1

## upstream patch 18.1
## upstream patch 19.1
## upstream patch 20.1

# Week 2

## upstream patch 20.1.1

############################################

# aggregate

tkg3 = ["1.18.0", "1.19.0", "1.20.0"] + ["1.18.1", "1.19.1", "1.20.1"]
tkg4 = ["1.19.0", "1.20.0", "1.21.0"] + ["1.19.1", "1.20.1"]
tkg5 = ["1.20.0", "1.21.0", "1.22.0"] + ["1.20.1"]