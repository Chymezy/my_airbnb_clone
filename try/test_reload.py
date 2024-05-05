from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
items = []

print("-- Reloaded objects --")
for v in all_objs.values():
    obj_str = f"[{v.__class__.__name__}] ({v.id}) {v.__dict__}"
    items.append(obj_str)
    # print(obj_str)

# Now items contains all the formatted strings inside a list
print(items)