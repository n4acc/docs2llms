# Supported Machines | fal.ai Docs


> Learn about the different machine types supported by fal, including specifications and how to set the machine type for your fal functions.


# Supported Machines

The fal runtime lets you specify the size of the machine that your fal functions run on. This is done using themachine_typeargument in thefal.functiondecorator. Currently, the following following options are available:

For example:

```
@fal.function(machine_type="GPU")defmy_function():...@fal.function(machine_type="L")defmy_other_function():...
```

```
@fal.function(machine_type="GPU")defmy_function():...@fal.function(machine_type="L")defmy_other_function():...
```

```
@fal.function(machine_type="GPU")
```

```
defmy_function():
```

```
...
```

```
@fal.function(machine_type="L")
```

```
defmy_other_function():
```

```
...
```

By default, themachine_typeis set toXS.

You can also switch the machine type of an existing fal function by using theonmethod.

```
my_function_S=my_function.on(machine_type="S")
```

```
my_function_S=my_function.on(machine_type="S")
```

```
my_function_S=my_function.on(machine_type="S")
```

In the above example,my_function_Sis a new fal function that has the same contents asmy_function, but it will run on a machine typeS.

Both functions can be called:

```
my_function()# executed on machine type `GPU`my_function_S()# same as my_function but executed on machine type `S`
```

```
my_function()# executed on machine type `GPU`my_function_S()# same as my_function but executed on machine type `S`
```

```
my_function()# executed on machine type `GPU`
```

```
my_function_S()# same as my_function but executed on machine type `S`
```

my_functionis executed on machine typeGPU. Andmy_function_S, which has the same logic asmy_function, is now executed on machine typeS.