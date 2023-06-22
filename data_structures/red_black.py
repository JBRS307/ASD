# drzewa czerwono-czarne - BST z dodatkowymi zasadami
#
# 1. Każdy węzeł jest czerwony albo czarny
# 2. Korzeń jest zawsze czarny
# 3. Każdy liść jest czarny (węzeł bez dzieci). W praktyce, każdy węzeł,
#    który nie ma dzieci, ma dzieci None, które są czarne
# 4. Jeśli węzeł jest czerwony, to obaj jego synowie są czarni
# 5. Każda prosta ścieżka z ustalonego węzła do liścia zawiera tyle samo czarnych węzłów