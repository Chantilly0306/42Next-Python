#include <stdlib.h>
#include <stdio.h>

// calculator lacks of the situation of parentheses so far
// ignore the Operator Precedence so far, so the operation sequence is from left to right

// ascii to float
float   ft_atof(char *str)
{
	int	    i = 0;
	int	    sign = 1;
	float	res = 0.0;
    float   div = 10.0;

	if (str[i] == '-')
	{
		sign *= -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		res = res * 10 + (str[i] - '0');
		i++;
	}
    if (str[i++] == '.')
    {
        while (str[i] >= '0' && str[i] <= '9')
	    {
		    res = res + (str[i] - '0') / div;
            div *= 10.0;
		    i++;
	    }
    }
	return (res * sign);
}

// ft_split
int	is_sep(char c, char *sep)
{
	int	i;

	i = 0;
	while (sep[i])
	{
		if (sep[i] == c)
			return (1);
		i++;
	}
	return (0);
}

int	count_word(char *str, char *sep)
{
	int	i;
	int	words;

	i = 0;
	words = 0;
	while (str[i])
	{
		if (!is_sep(str[i], sep) && (is_sep(str[i + 1], sep) || !str[i + 1]))
			words++;
		i++;
	}
	return (words);
}

int	count_c(char *str, char *sep, int j)
{
	int	c;

	c = 0;
	while (str[j] && !is_sep(str[j], sep))
	{
		c++;
		j++;
	}
	return (c);
}

char	*fill_c(char *str, int pos, int len)
{
	int		i;
	char	*word;

	word = malloc(sizeof(char) * (len + 1));
	if (!word)
		return (NULL);
	i = 0;
	word[len] = '\0';
	while (i < len)
	{
		word[i] = str[pos];
		i++;
		pos++;
	}
	return (word);
}

char	**ft_split(char *str, char *charset, int words)
{
	char	**res;
	int		i;
	int		pos;
	int		len;

	if (!str || !charset)
		return (NULL);
	res = malloc(sizeof(char *) * (words + 1));
	if (!res)
		return (NULL);
	res[words] = NULL;
	i = 0;
	pos = 0;
	while (i < words)
	{
		while (str[pos] && is_sep(str[pos], charset))
			pos++;
		len = count_c(str, charset, pos);
		res[i] = fill_c(str, pos, len);
		pos += len;
		i++;
	}
	return (res);
}

// calculator
int main(int argc, char **argv)
{
    char    **nbs;
    float   *floats;
    int     i = 0;
    int     j = 0;
    int     words;
    float   res;

    if (argc < 2)
        return (0);
    words = count_word(argv[1], "+-*/");
    nbs = ft_split(argv[1], "+-*/", words);
    floats = malloc(sizeof(float) * words);
    while (nbs[i])
    {
        floats[i] = ft_atof(nbs[i]);
        free(nbs[i]);
        i++;
    }
    free(nbs);
    res = floats[0];
    i = 1;
    while (argv[1][j])
    {
        if (argv[1][j] == '+')
            res += floats[i++];
        else if (argv[1][j] == '-')
            res -= floats[i++];
        else if (argv[1][j] == '*')
            res *= floats[i++];
        else if (argv[1][j] == '/')
            res /= floats[i++];
        j++;
    }
    free(floats);
    printf("%s = %.4f\n", argv[1], res);
}
