'''
Any letter = *
Any Number = +

Formats of first part of UK postcodes:
[**+*]- ie. EC1-EC4,NW1W,SE1P,SW1 with WC postcode area
[*+*]- for areas E1, N1, W1

[*+] or [*++] - for areas with first letter B, E, G, L, M, N, S, W
[**+] or [**++]- for all other area codes
all postcodes end with the format [+**]
not used in first position: Q,V,X
not used in second position: I,J,Z
for second part of postcode [+**]- Letters C, I, K, M, O, V not used, looks too similar to numbers when hand-written
for postcode formats [*+*], the third letter only has: A, B, C, D, E, F,G,H,J,K,P,S,T,U
for postcode formats [**+*], the fourth letter can be: A, B, E, H, M, N, P, R, V, W, X, Y
'''
