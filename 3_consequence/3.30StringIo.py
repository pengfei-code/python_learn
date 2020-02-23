#stringio
import io
a = "hello world"
b = io.StringIO(a)

print(b.getvalue())

b.seek(1)
b.write('g')

print(b.getvalue())

b.write("eeee")
print(b.getvalue())

print(type(a))
