# Is there something suspicious about the following code?
# What changed from the previous example

const GRAVITY : float = 10

var velocity : Vector2 = Vector2(0,0)
var speed : float = 500
var jump_power : float = 1000

func _physics_process():

    velocity.y += GRAVITY

    if Input.is_action_pressed("ui_up"):
        velocity.y = -jump_power

    velocity.x = Input.get_axis("ui_left","ui_right") * speed

    