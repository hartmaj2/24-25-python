# What happens when player holds both left and right arrow keys

const GRAVITY : float = 10

var velocity : Vector2 = Vector2(0,0)
var speed : float = 500
var jump_power : float = 1000

func _physics_process():

	velocity.y += GRAVITY # falling

	if Input.is_action_just_pressed("ui_up"):
		velocity.y = -jump_power
	if Input.is_action_pressed("ui_right"):
		velocity.x = speed
	elif Input.is_action_pressed("ui_left"):
		velocity.x = -speed
	else:
		velocity.x = 0