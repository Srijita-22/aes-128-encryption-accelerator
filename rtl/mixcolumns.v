module mixcolumns (
    input  wire [31:0] col_in,
    output wire [31:0] col_out
);

wire [7:0] s0,s1,s2,s3;
wire [7:0] m2_0,m2_1,m2_2,m2_3;
wire [7:0] m3_0,m3_1,m3_2,m3_3;

assign s0 = col_in[31:24];
assign s1 = col_in[23:16];
assign s2 = col_in[15:8];
assign s3 = col_in[7:0];

gf_mult2 g0(.data_in(s0), .data_out(m2_0));
gf_mult2 g1(.data_in(s1), .data_out(m2_1));
gf_mult2 g2(.data_in(s2), .data_out(m2_2));
gf_mult2 g3(.data_in(s3), .data_out(m2_3));

gf_mult3 h0(.data_in(s0), .data_out(m3_0));
gf_mult3 h1(.data_in(s1), .data_out(m3_1));
gf_mult3 h2(.data_in(s2), .data_out(m3_2));
gf_mult3 h3(.data_in(s3), .data_out(m3_3));

assign col_out[31:24] = m2_0 ^ m3_1 ^ s2   ^ s3;
assign col_out[23:16] = s0   ^ m2_1 ^ m3_2 ^ s3;
assign col_out[15:8]  = s0   ^ s1   ^ m2_2 ^ m3_3;
assign col_out[7:0]   = m3_0 ^ s1   ^ s2   ^ m2_3;

endmodule
