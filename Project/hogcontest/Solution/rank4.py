import numpy as D,lzma,base64 as E
PLAYER_NAME='桜風の誓い'
C=lzma.decompress(E.b64decode('/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4AThAo5dABmCfAqujrowZ5M4DkXaFK998qDAe8wi2y8TF1M1GCCurcLSRapnDzpsHHifDxxWEi6TnBKilQVm+JVW1ajNKlB/PFh9zC0gdy/GVk+zfNCTfxiSPMGrpH4jCn/yptCEyPIZbM8mUK3qa2sXgmQw1GAYK+36PXh4r+vcuIWX/5oU28gwcQi+j113hV1OCO80CyQ/Fk/k4vK2BkdcLjy3M4cABHwVdDNFPFavW6Uwx29i5qdrCzW3s/fnU3Tsp3AJ0eM+RWW4WpdnMdiWHFVo9sWH56LKn97PglKoWZY9S21aZcHsr9AaOosvHdI8WGGOCTUUQfkY+nsyEgxmp8fGLT4uBT5HqmEXcgKUc3TGLp295lwbqIU7tfru4hPNAaSQtWSXBCVXoPSfnbR97olPXd4zTvpcyzaS4ENULVxRUoExkfR2aiPmU9D6xN7NxWS0cPM8F0ywv06X5BPl31i03/p91Eqv18Kt0sxQkYXVsHr5cVwiqugYfdTEt3dPqU0MAEaTOoVX6TmA7PSZhGue6arnx4u5Ndrs/OF4gURx2A58H2f3Qc1C3kgw+1FwC4g5bODaZiNnumETvUi7cXOGGSDfWLqfcXTK29dXCABZXnSjo2EMC06wg5+71DmPzwJLV4x8ucYRA66rhJTMnnA9PJsSnmTGj7j9szGT1PiJ98+daYuSp5bYYSb4a/qbTWa2f+StIE0z/VusKXATk/Nf9fZnJcNWXGnCHcpLBlKauOdQCKzX2cZUy/hwgSEJGh8LoXGzFZn/yPkOeP6M0wlZbnXh8kpVr1Rweg9/QZQW6RnHPH5m8wdwXW/29KeiIl/wgAzBI81czcTvLjMrm7Ci9/c9WDG/V91wgjoLpiHvAAAAAEBmXR2RiKkfAAGqBeIJAAAZ25XAscRn+wIAAAAABFla'))
B=D.zeros(2500)
for A in range(1250):B[A*2],B[A*2+1]=C[A]&15,C[A]>>4
def final_strategy(s,os):return int(B[s%50+(os%50)*50])