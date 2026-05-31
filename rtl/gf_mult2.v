module gf_mult2(
    input  wire [7:0] data_in,
    output wire [7:0] data_out
);

assign data_out =
    data_in[7] ?
    ((data_in << 1) ^ 8'h1b) :
    (data_in << 1);

endmodule
