from count_words import CountWords

# 1. IF true [V and (V or F)]
# 2. IF true [F or V]
def test_two_words_ending_with_s():
    words = CountWords().count("dogs cats")
    assert words == 2

# 1. IF false [V and (F or F)] 
# 2. IF false [F or F]
def test_no_words_at_all(): 
    words = CountWords().count("dog cat")
    assert words == 0

# 1. IF true [V and (F or V)] 
# 2. IF true [V or F]
def test_words_that_end_in_r():
    words = CountWords().count("car bar")
    assert words == 2

# 1. IF true [V and (F or V)] 
# 2. IF true [F or V]
def test_mixed_endings():
    words = CountWords().count("car cats")
    assert words == 2

# 1. IF false [F and (F or F)] 
# 2. IF True [F or V]
def test_word_ending_with_s_at_end():
    words = CountWords().count("cats")
    assert words == 1

# 1. IF True [V and (V or F)] 
# 2. IF False [F or F]
def test_non_alpha_characters():
    words = CountWords().count("dogs, cats.")
    assert words == 2

# 1. IF (no entra al bucle) 
# 2. IF false (F or F)
def test_empty_string():
    words = CountWords().count("")
    assert words == 0

# 1. IF false [V and (F or F))]
# 2. IF false [V or V]
def test_only_non_alpha():
    words = CountWords().count("!!!")
    assert words == 0

#### IF verdaderos ####

# [V and (F or V)]
def test_first_if_true():
    words = CountWords().count("daughter son")
    assert words == 1

# [F or V]
def test_second_if_true():
    words = CountWords().count("$&!/s")
    assert words == 1

#### IF Falsos ####

# [V and (F or F)]
def test_first_if_false():
    words = CountWords().count("silva quispe ravichagua")
    assert words == 0

# [F or F]
def test_second_if_false():
    words = CountWords().count("supabase")
    assert words == 0
  
    
###CASO MINUSCULA###

def test_two_words_ending_with_capital_S():
    words = CountWords().count("DogS catS")
    assert words == 2

def test_one_words_ending_with_capital_S():
    words = CountWords().count("Dogs catS")
    assert words == 2

def test_all_in_capital_mixed():
    words = CountWords().count("CAR DOGS")
    assert words == 2

def test_only_one_capital_S():
    words = CountWords().count("CAt DOGS")
    assert words == 1

def test_only_one_capital_R():
    words = CountWords().count("CAr DOG")
    assert words == 1