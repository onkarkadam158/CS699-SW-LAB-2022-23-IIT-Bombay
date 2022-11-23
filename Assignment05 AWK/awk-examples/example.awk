BEGIN {
  FS=",";
  OFS=",";
}

{
  if($3 ~ /Mariana/) {
    M++;
  } else if($3 ~ /Nile/) {
    N++;
  } else {
    B++;
  }
}

END {
  print B, N, M;
}
