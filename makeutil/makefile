.PHONE: another-app
# not all target are listed in PHONE

# might be correct, but 'build' and 'app' are different
build:
	gcc main.c -o app


# correct no PHONE
app: main.c
	gcc main.c -o app


# incorrect: listed PHONE
another-app: main.c
	gcc main.c -o another-app