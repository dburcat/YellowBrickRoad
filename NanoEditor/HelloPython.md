# Hello Python using NanoEditor

Open the terminal and type `nano yowza.py`.

TYPE in the following text:

```python
print("Yowza!")
i = 42
print(i)
d = 2.71828
print(d)
s = "ZipCode Rocks!"
print(s)
```

Save the file.
Exit the editor


Open the terminal and type `nano hello.py`.

TYPE in the following text:

```python
def main():
    print("Hello, Python!")

if __name__ == "__main__":
    main()
```

Save the file.
Exit the editor

- Run the program using `python hello.py`

What happened? Did you see the output `Hello, Python!`?

Now, let's try something else.

Edit hello.py using `nano`.

Add the following line of code:

```python
print("Hello, again!")
```

Make sure you put it inside the `main` function, right after the `Hello, Python` line.
Save the file. Exit the editor.

Run the program again.

What happened? Did you see the output `Hello, Python!` and `Hello, again!`?

Good. Now save all this to your GitHub repository.

```bash
git add .
git commit -m "Add Hello Python work, finished"
git push
```
