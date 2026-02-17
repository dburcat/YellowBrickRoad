# Hello Java using NanoEditor

Open the terminal and type `nano Yowza.jsh`.

TYPE in the following text:

```java
System.out.println("Yowza!");
int i = 42;
System.out.println(i);
double d = 2.71828;
System.out.println(d);
String s = "ZipCode Rocks!";
```

Save the file.
Exit the editor


Open the terminal and type `nano Hello.java`.

TYPE in the following text:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

Save the file.
Exit the editor

- Compile the file using `javac Hello.java`
- Run the program using `java Hello`

What happened? Did you see the output `Hello, Java!`?

Now, let's try something else.

Edit Hello.java using `nano`.

Add the following line of code:

```java
System.out.println("Hello, again!");
```

Make sure you put it inside the `main` method, right after the `Hello, Java` line.
Save the file. Exit the editor.

Compile and run the program again.

What happened? Did you see the output `Hello, Java!` and `Hello, again!`?

Good. Now save all this to your GitHub repository.

```bash
git add .
git commit -m "Add Hello Java work, finished"
git push
```
