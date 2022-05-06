# Simple Generator For Secret keys and Password.

## Import Class.

```python
from Generator import Generator
generator = Generator()
```

## Get Secret keys With Details Like Length of Key.

```python
secret_key_With_details  = generator.Secret_Key()
```

Out Put.

> Secret key With Details is: ('4NBxiKvnusEvkR4015dJPuBVgxK2', 'Size: 28', 'Size Without separated: 28')

## Without Details.

```python
secret_key_Without_details  = generator.Secret_Key(Out_Put_ID_Only = True)
```

Out Put.

> Secret key Without Details is: OAb1D9vPbu8OY845KdcAx0PyYpRg

## With separated.

```python
secret_key_With_Separated = generator.Secret_Key(Separated = "-")
```

OutPut.

> Secret key With Separated is: ('vxBUGQfW-9OKH-c6dM-0TUfKF8pInP1', 'Size: 31', 'Size Without Separated: 28')

## Password.

```python
Password = generator.Password()
```

OutPut.

> Password is: WyNAfehHP2zGFrsk36Rtwgj#5oDd

## Password With Special Character.

```python
Password_With_Special_Chara = generator.Password(Special_Chara = "\\|")
```

OutPut.

> Secret key with Special Character is: 5nWVX2sSYELNi|BZe1Mmk#!awgo$

## Change Length & Number_of_Each_Separated.

```python
secret_key_With_details  = generator.Secret_Key(Length = 48, Number_of_Each_Separated = [12,6,6,24], Separated = "=+=")
secret_key_With_details  = generator.Secret_Key(Length = 36, Number_of_Each_Separated = [8,4,4,4,16], Separated = "-")
```

OutPut.

> Secret key With 4 Separation is: ('VvJbw4t9HifQ=+=TPQ43F=+=8XYN7W=+=2W8rMXm4KZlup7GwEO5hRs3k', 'Size: 57', 'Size Without Sptreated: 48')
> Secret key With 5 Separation is: ('ztrVniD4-pzjK-ydkU-YAhV-p8DFIgyPne3v5Mcw', 'Size: 40', 'Size Without Sptreated: 36')
