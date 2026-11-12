1. Queenside castling moves rook to wrong square; `s[c+3*m]` fails for a-file. `Y`, line 62: `s[c+m],s[c+3*m-int(m<0)]=s[c+3*m-int(m<0)],h`
2. Iterative deepening can return `None` if no moves at depth 1. `C`, line 84: `E=i[0] if i else r`
3. Quiescence search lacks check awareness; it may return a static eval while in check. `D`, line 68: `if J(a,a.index('kK'[d==l]),'wb'[d==l]):return G(a,d,g,f,1,j,A,k)`
4. MVV-LVA ordering assigns 0 value to kings; captures of high-value pieces by king are ordered low. `T/d`, line 2: `d=100,320,330,500,900,1e6`
5. Evaluator is purely material; lacks simple piece-square tables or mobility. `x`, line 25: `sum((-1+2*q.isupper())*(d[T.index(q.lower())]+bonus[i]) for i,q in enumerate(a)...)`
6. F