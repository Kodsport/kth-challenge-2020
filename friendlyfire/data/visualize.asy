defaultpen(1.5);
size(1000, 500);
pen shadow = rgb(1, 0.75, 0.75);

// Read input
int n = stdin;
int m = stdin;

path[] lines;
write("draw boats");
for (int i = 0; i < m; ++i) {
  real x1 = stdin, x2 = stdin, y = stdin;
  fill((x1-0.5, y) -- (x2+0.5, y) -- ((x1+x2)/2.0, y-(x2-x1+1)/2.) -- cycle, shadow);
  lines.push((x1-0.5, y) -- (x2+0.5, y));
}
for (int i = 0; i < m; ++i) {
  draw(lines[i], red);
}

draw((-n, n) -- (0, 0) -- (n, n), black+dashed);
string sol = stdin; // eat newline
sol = stdin;
if (sol != "impossible") {
  write("draw sol");
  int x = 0, y = 0;
  guide p = (0, 0);
  for (int i = 0; i < n; ++i) {
    y += 1;
    string step = substr(sol, i, 1);
    if (step == '+') x += 1;
    else if (step == '-') x -= 1;
    if (i == n-1 || step != substr(sol, i+1, 1)) {
      p = p -- (x, y);
    }
  }
  draw(p, blue+4);
}

clip((-n, 0) -- (n, 0) -- (n, n) -- (-n, n) -- cycle);
write("render");
shipout(bbox(xmargin=5, white, Fill));
