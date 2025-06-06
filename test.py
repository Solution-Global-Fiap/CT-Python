from main import calculate_raindrop_force, calculate_raindrop_type, classify_rain

def test_calculate_raindrop_force():
    assert calculate_raindrop_force(1.0, 2.0) == 2.0
    assert calculate_raindrop_force(0.5, 4.0) == 2.0
    assert calculate_raindrop_force(0.0, 10.0) == 0.0
    assert calculate_raindrop_force(2.0, 0.0) == 0.0

def test_calculate_raindrop_type():
    assert calculate_raindrop_type(0.00129) == "Light"
    assert calculate_raindrop_type(0.00130) == "Moderate"
    assert calculate_raindrop_type(0.00179) == "Moderate"
    assert calculate_raindrop_type(0.00180) == "Heavy"
    assert calculate_raindrop_type(0.00200) == "Heavy"

def test_classify_rain():
    # Classifica com todas gotas leves
    drops = [(0.5, 0.002), (0.6, 0.001), (0.7, 0.001)]
    assert classify_rain(drops) == "Light"
    # Classifica com todas as gotas médias
    drops = [(1.0, 0.0013), (1.0, 0.0015), (1.0, 0.00179)]
    assert classify_rain(drops) == "Moderate"
    # Classifica com todas as gotas pesadas
    drops = [(1.0, 0.002), (1.0, 0.0021), (1.0, 0.0022)]
    assert classify_rain(drops) == "Heavy"
    # Classifica com gotas leves, médias e pesadas, porém contendo mais gotas pesadas
    drops = [(1.0, 0.002), (1.0, 0.0021), (1.0, 0.001), (1.0, 0.001)]
    assert classify_rain(drops) == "Light"
    # Classifica com gotas leves, médias e pesadas, porém contendo mais gotas médias
    drops = [(1.0, 0.0015), (1.0, 0.0016), (1.0, 0.001), (1.0, 0.002)]
    assert classify_rain(drops) == "Moderate"
    # Classifica com gotas leves, médias e pesadas, porém contendo mais gotas pesadas
    drops = [(1.0, 0.002), (1.0, 0.0016), (1.0, 0.001), (1.0, 0.002)]
    assert classify_rain(drops) == "Heavy"

test_calculate_raindrop_force()
test_calculate_raindrop_type()
test_classify_rain()