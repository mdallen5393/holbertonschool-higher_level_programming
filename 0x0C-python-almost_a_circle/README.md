# PROJECT: 0x09. Python - Almost a circle
### AUTHOR: Matthew Allen

## TASKS:
### 0. If it's not tested it doesn't work - tests/
All files, classes and methods must be unit tested and PEP8 validated.

### 1. Base class - models/base.py, models/__init__.py
Class `Base` with private class attribute `__nb_objects`, a constructor that takes an `id`.

### 2. First Rectangle - models/rectangle.py
Class `Rectangle` that inherits from `Base`, with private instance attributes for width, height, x, y, and a constructor.

### 3. Validate attributes - models/rectangle.py
Updates class `Rectangle` by adding validation of all setter methods and instantiation.

### 4. Area first - models/rectangle.py
Updates class `Rectangle` by adding the public `area` method which returns the area value of the `Rectangle` instance.

### 5. Display #0 - models/rectangle.py
Updates class `Rectangle` by adding the public `display` method that prints the `Rectangle` instance with the character `#`, without handling `x` and `y`.

### 6. \__str__ - models/rectangle.py
Updates class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.

### 7. Display #1 - models/rectangle.py
Updates class `Rectangle` by improving the public `display` method to take care of `x` and `y`.

### 8. Update #0 - models/rectangle.py
Updates class `Rectangle` by adding the public `update` method that assigns arguments to each attribute.

### 9. Update #1 - models/rectangle.py
Updates class `Rectangle` by updating the public `update` method by changing the prototype to include `*args` and `**kwargs`.

### 10. And now, the Square! - models/square.py
Class `Square` that inherits from `Rectangle`.

### 11. Square size - models/square.py
Updates class `Square` by adding the public getter and setter `size`.

### 12. Square update - models/square.py
Updates class `Square` by adding the public `update` method that assigns attributes.

### 13. Rectangle instance to dictionary representation - models/rectangle.py
Updates class `Rectangle` by adding the public `to_dictionary` method that returns the dictionary representation of a `Rectangle`.

### 14. Square to instance to dictionary representation - models/square.py
Updates class `Square` by adding the public method `to_dictionary` that returns the dictionary representation of a `Square`.

### 15. Dictionary to JSON string - models/base.py
Updates class `Base` by adding the static method `to_json_string` that returns the JSON string representation of `list_dictionaries`.

### 16. JSON string to file - models/base.py
Updates class `Base` by adding the class method `save_to_file` that writes the JSON string representation of `list_objs` to a file.

### 17. JSON string to dictionary - models/base.py
Updates class `Base` by adding the static method `from_json_string` that returns the list of the JSON string representation `json_string`.

### 18. Dictionary to Instance - models/base.py
Updates class `Base` by adding the class method `create` that returns an instance with all attributes already set.

### 19. File to instances - models/base.py
Updates class `Base` by adding the class method `load_from_file` that returns a list of instances.
