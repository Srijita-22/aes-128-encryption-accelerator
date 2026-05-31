module gf_mult3(
    input  wire [7:0] data_in,
    output wire [7:0] data_out
);

wire [7:0] mult2;

gf_mult2 u1(
    .data_in(data_in),
    .data_out(mult2)
);

assign data_out = mult2 ^ data_in;

endmodule
