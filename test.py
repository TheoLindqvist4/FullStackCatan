def scale_dimensions(scale_of_widget):
    dimension_image = [666,375]
    new_dimension= []
    # Leaving 50 pixels on each side for better visibility
    new_dimension[0] = scale_of_widget[0]-100
    new_dimension[0] = scale_of_widget[1]-100

    scale_image = new_dimension[0]/5
    scale_image_overlap = scale_image*1.25

    new_dimension_image= []
    factor = scale_image_overlap / dimension_image[0]
    new_dimension_image[0] = dimension_image[0] * factor
    new_dimension_image[1] = dimension_image[1] * factor
 
    #Create the position of the middle tile for each row
    #Row 1 has only 3 tiles
    positionnning_middle_tile_row_1 = [new_dimension[0]/2 , new_dimension[0] - scale_image_overlap/2]
    positionnning_first_tile_row_1 = [new_dimension[0]/2 - new_dimension_image[1] , new_dimension[0] - scale_image_overlap/2]
    positionnning_last_tile_row_1 = [new_dimension[0]/2 + new_dimension_image[1] , new_dimension[0] - scale_image_overlap/2]

    #Row 2 has 4 tiles

    positionnning_middle_left_tile_row_2 = [new_dimension[0]/2 - new_dimension_image[1]/2, new_dimension[0] - scale_image_overlap/2 - scale_image]
    positionnning_middle_left_minus_1_tile_row_2 = [new_dimension[0]/2 - new_dimension_image[1]/2 - new_dimension_image[1], new_dimension[0] - scale_image_overlap/2 - scale_image]
    positionnning_middle_right_tile_row_2 = [new_dimension[0]/2 + new_dimension_image[1]/2, new_dimension[0] - scale_image_overlap/2 - scale_image]
    positionnning_middle_right_plus_1_tile_row_2 = [new_dimension[0]/2 + new_dimension_image[1]/2 + new_dimension_image[1], new_dimension[0] - scale_image_overlap/2 - scale_image]


    # Row 3 has 5 tiles
    positionnning_middle_tile_row_3 = [new_dimension[0]/2 , new_dimension[0] - scale_image_overlap/2 - 2 * scale_image]
    positionnning_middle_minus_1_tile_row_3 = [new_dimension[0]/2 - new_dimension_image[1] , new_dimension[0] - scale_image_overlap/2 - 2 * scale_image]
    positionnning_middle_minus_2_tile_row_3 = [new_dimension[0]/2 - 2 * new_dimension_image[1] , new_dimension[0] - scale_image_overlap/2 - 2 *scale_image]
    positionnning_middle_plus_1_tile_row_3 = [new_dimension[0]/2 + new_dimension_image[1] , new_dimension[0] - scale_image_overlap/2 - 2 * scale_image]
    positionnning_middle_plus_2_tile_row_3 = [new_dimension[0]/2 + 2* new_dimension_image[1] , new_dimension[0] - scale_image_overlap/2 - 2 * scale_image]

    #Row 4 has 4 tiles

    positionnning_middle_left_tile_row_4 = [new_dimension[0]/2 - new_dimension_image[1]/2, new_dimension[0] - scale_image_overlap/2 - 3* scale_image]
    positionnning_middle_left_minus_1_tile_row_4 = [new_dimension[0]/2 - new_dimension_image[1]/2 - new_dimension_image[1], new_dimension[0] - scale_image_overlap/2 - 3* scale_image]
    positionnning_middle_right_tile_row_4 = [new_dimension[0]/2 + new_dimension_image[1]/2, new_dimension[0] - scale_image_overlap/2 - 3* scale_image]
    positionnning_middle_right_plus_1_tile_row_4 = [new_dimension[0]/2 + new_dimension_image[1]/2 + new_dimension_image[1], new_dimension[0] - scale_image_overlap/2 - 3* scale_image]

    #Row 5 has only 3 tiles
    positionnning_middle_tile_row_5 = [new_dimension[0]/2 , new_dimension[0] - scale_image_overlap/2 - 4 * scale_image]
    positionnning_first_tile_row_5 = [new_dimension[0]/2 - new_dimension_image[1] , new_dimension[0] - scale_image_overlap/2 - 4 * scale_image]
    positionnning_last_tile_row_5 = [new_dimension[0]/2 + new_dimension_image[1] , new_dimension[0] - scale_image_overlap/2 - 4 * scale_image]


def available_spots(self, scale_of_widget,dimension_image_tile):
        dimension_image = [168,168]
        dimension_image_tile = [
            scale_of_widget[0] - 100,
            scale_of_widget[1] - 100
        ]

        scale_image = dimension_image_tile[0] / 5
        scale_image_overlap = scale_image * 1.3245

        factor_available_spots = scale_image_overlap/5
    
        new_dimension_image = [
            dimension_image[0] * factor_available_spots,
            dimension_image[1] * factor_available_spots
        ]

        # Calculate positions based on new dimensions
        positions = {
            1: [
                [dimension_image_tile[0] / 2 - new_dimension_image[0],0],
                [dimension_image_tile[0] / 2, 0],
                [dimension_image_tile[0] / 2 + new_dimension_image[0], 0]
            ],
            2: [
                [dimension_image_tile[0] / 2 - new_dimension_image[0],scale_image],
                [dimension_image_tile[0] / 2, scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0], scale_image]  
            ],

            3: [
                [dimension_image_tile[0] / 2 - 1.5 * new_dimension_image[0], scale_image],
                [dimension_image_tile[0] / 2 - new_dimension_image[0] / 2, scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0] / 2, scale_image],
                [dimension_image_tile[0] / 2 + 1.5 * new_dimension_image[0],scale_image]
            ],

            4: [
                [dimension_image_tile[0] / 2 - 1.5 * new_dimension_image[0], 2*scale_image],
                [dimension_image_tile[0] / 2 - new_dimension_image[0] / 2, 2*scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0] / 2, 2*scale_image],
                [dimension_image_tile[0] / 2 + 1.5 * new_dimension_image[0], 2*scale_image]
            ],

            5: [
                [dimension_image_tile[0] / 2 - 2 * new_dimension_image[0], 2* scale_image],
                [dimension_image_tile[0] / 2 - new_dimension_image[0], 2*scale_image],
                [dimension_image_tile[0] / 2, 2*scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0], 2*scale_image],
                [dimension_image_tile[0] / 2 + 2 * new_dimension_image[0], 2*scale_image]
            ],

            6: [
                [dimension_image_tile[0] / 2 - 2 * new_dimension_image[0], 3* scale_image],
                [dimension_image_tile[0] / 2 - new_dimension_image[0], 3*scale_image],
                [dimension_image_tile[0] / 2, 3*scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0], 3*scale_image],
                [dimension_image_tile[0] / 2 + 2 * new_dimension_image[0], 3*scale_image]
            ],

            7: [
                [dimension_image_tile[0] / 2 - 1.5 * new_dimension_image[0], 3*scale_image],
                [dimension_image_tile[0] / 2 - new_dimension_image[0] / 2, 3*scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0] / 2, 3*scale_image],
                [dimension_image_tile[0] / 2 + 1.5 * new_dimension_image[0], 3*scale_image]
            ],

            8: [
                [dimension_image_tile[0] / 2 - 1.5 * new_dimension_image[0], 4*scale_image],
                [dimension_image_tile[0] / 2 - new_dimension_image[0] / 2, 4*scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0] / 2, 4*scale_image],
                [dimension_image_tile[0] / 2 + 1.5 * new_dimension_image[0], 4*scale_image]
            ],

            9: [
                [dimension_image_tile[0] / 2 - new_dimension_image[0], 4*scale_image],
                [dimension_image_tile[0] / 2, 4*scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0], 4*scale_image]
            ],

            10: [
                [dimension_image_tile[0] / 2 - new_dimension_image[0], 5*scale_image],
                [dimension_image_tile[0] / 2, 5*scale_image],
                [dimension_image_tile[0] / 2 + new_dimension_image[0], 5*scale_image]
            ]
        }

        return new_dimension_image, positions
