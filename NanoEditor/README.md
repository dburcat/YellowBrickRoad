# NanoEditor

Learn to use `nano` to edit text files.

> `fork` this repository and `clone` it to your local machine.

What is a text editor?

A text editor is a program that allows you to create and edit text files.
Text editors are used to write code, take notes, and create documents.
There are many different text editors available, each with its own features and capabilities.

We will be using `nano`, a simple and easy-to-use text editor that is available on most Unix-based systems.

## Getting Started

To get started, open a terminal window on your computer.

Type `nano`

You should see a blank screen with a few lines of information at the bottom.
Notice what you can "do" with `nano` at the bottom of the screen.

## Basic Commands

Here are some basic commands you can use in `nano`:

- `Ctrl-O`: Write Out (save) the current file
- `Ctrl-X`: Exit the editor
- `Ctrl-G`: Get Help
- `Ctrl-C`: Show Cursor Position

But what does `Crtl-` mean? It means to hold down the `control` key while pressing the other key.
`control` works like `shift`, but you cannot see the difference on the screen.

## Editing Text

To edit text in `nano`, simply start typing.
You can move the cursor around using the arrow keys on your keyboard.

Paste in this text:

```markdown
# NanoEditor

Learn to use `nano` to edit text files.
```

## Saving Your Work

To save your work in `nano`, press `Ctrl-O`.
You will be prompted to enter a filename.

Type `simple.md` and press `Enter`.

Now exit the editor by pressing `Ctrl-X`.

## Viewing Your File

To view the file you just created, type `cat simple.md` in the terminal.

You should see the text you entered in `nano`.

## Editing an Existing File

To edit an existing file with `nano`, type `nano simple.md` in the terminal.

You can now edit the file as you did before.
Add the following text to the file:

```markdown
What is a text editor?

A text editor is a program that allows you to create and edit text files.
```

Save your changes by pressing `Ctrl-O` and then exit `nano` by pressing `Ctrl-X`.

Verify that the changes were saved by typing `cat simple.md` in the terminal.

## Conclusion

You have now learned how to use `nano` to create and edit text files. (Just the very basics)

See Hello.java with `nano` in the next file [HelloJava.md](HelloJava.md).
See Hello.py with `nano` in the next file [HelloPython.md](HelloPython.md).

And for more advanced text editing, see [Nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html).
