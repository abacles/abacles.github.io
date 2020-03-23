#include <stdio.h>

int main()
{
  FILE *out = fopen("ascii.out","w");
  char ch;
  for(ch=33;ch<127;ch++)
    {
      fprintf(out,"<tr>\n");
      fprintf(out,"<td>%d</td>\n",ch);
      fprintf(out,"<td>%c</td>\n",ch);
      fprintf(out,"</tr>\n");
    }
  fclose(out);
}
